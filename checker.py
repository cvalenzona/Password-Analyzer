"""
Password Strength Analyzer - Core Logic
Analyzes password security and provides recommendations
"""

import re
from typing import Dict, List

class PasswordAnalyzer:
    """Analyzes password strength and provides recommendations"""
    
    # Common weak passwords to check against
    COMMON_PASSWORDS = [
        'password', '123456', 'password123', 'admin', 'letmein',
        'welcome', 'monkey', 'dragon', 'master', 'qwerty',
        'abc123', 'login', 'passw0rd', 'iloveyou', 'sunshine'
    ]
    
    # Keyboard patterns to detect
    KEYBOARD_PATTERNS = [
        'qwerty', 'asdfgh', 'zxcvbn', '12345', 'qazwsx', 'qweasd'
    ]
    
    def __init__(self, password: str):
        """Initialize with password to analyze"""
        self.password = password
        self.score = 0
        self.feedback = []
        self.strength_level = ""
        
    def analyze(self) -> Dict:
        """Run full analysis and return results"""
        self.score = 0
        self.feedback = []
        
        # Run all checks
        self._check_length()
        self._check_uppercase()
        self._check_lowercase()
        self._check_numbers()
        self._check_special_chars()
        self._check_common_passwords()
        self._check_keyboard_patterns()
        self._check_repeated_chars()
        
        # Determine strength level
        self._set_strength_level()
        
        return {
            'password': '***' if self.password else '',  # Don't return actual password
            'score': self.score,
            'strength': self.strength_level,
            'feedback': self.feedback,
            'length': len(self.password),
            'recommendations': self._get_recommendations()
        }
    
    def _check_length(self) -> None:
        """Check password length (Step 1)"""
        length = len(self.password)
        
        if length == 0:
            self.feedback.append("❌ Password is empty")
            return
        
        if length < 8:
            self.feedback.append(f"⚠️ Too short ({length} chars). Use at least 8 characters")
            self.score += 10
        elif length < 12:
            self.feedback.append(f"✅ Good length ({length} chars)")
            self.score += 20
        elif length >= 12:
            self.feedback.append(f"✅ Excellent length ({length} chars)")
            self.score += 25
    
    def _check_uppercase(self) -> None:
        """Check for uppercase letters"""
        if re.search(r'[A-Z]', self.password):
            self.feedback.append("✅ Contains uppercase letters")
            self.score += 15
        else:
            self.feedback.append("⚠️ Missing uppercase letters (A-Z)")
    
    def _check_lowercase(self) -> None:
        """Check for lowercase letters"""
        if re.search(r'[a-z]', self.password):
            self.feedback.append("✅ Contains lowercase letters")
            self.score += 15
        else:
            self.feedback.append("⚠️ Missing lowercase letters (a-z)")
    
    def _check_numbers(self) -> None:
        """Check for numbers"""
        if re.search(r'[0-9]', self.password):
            self.feedback.append("✅ Contains numbers")
            self.score += 15
        else:
            self.feedback.append("⚠️ Missing numbers (0-9)")
    
    def _check_special_chars(self) -> None:
        """Check for special characters"""
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'\",.>?/\\|`~]', self.password):
            self.feedback.append("✅ Contains special characters")
            self.score += 20
        else:
            self.feedback.append("⚠️ Missing special characters (!@#$%^&*)")
    
    def _check_common_passwords(self) -> None:
        """Check against common passwords"""
        password_lower = self.password.lower()
        
        for common in self.COMMON_PASSWORDS:
            if common in password_lower:
                self.feedback.append(f"🚨 Contains common word: '{common}'")
                self.score = max(0, self.score - 10)
                return
        
        self.feedback.append("✅ Not a common password")
    
    def _check_keyboard_patterns(self) -> None:
        """Check for keyboard patterns"""
        password_lower = self.password.lower()
        
        for pattern in self.KEYBOARD_PATTERNS:
            if pattern in password_lower:
                self.feedback.append(f"🚨 Contains keyboard pattern: '{pattern}'")
                self.score = max(0, self.score - 10)
                return
        
        self.feedback.append("✅ No obvious keyboard patterns")
    
    def _check_repeated_chars(self) -> None:
        """Check for excessive repeated characters"""
        if re.search(r'(.)\1{2,}', self.password):
            self.feedback.append("⚠️ Contains repeated characters (aaa, 111, etc)")
            self.score = max(0, self.score - 5)
        else:
            self.feedback.append("✅ No excessive repeated characters")
    
    def _set_strength_level(self) -> None:
        """Determine strength level based on score"""
        if self.score <= 20:
            self.strength_level = "Very Weak"
        elif self.score <= 40:
            self.strength_level = "Weak"
        elif self.score <= 60:
            self.strength_level = "Fair"
        elif self.score <= 80:
            self.strength_level = "Good"
        else:
            self.strength_level = "Strong"
    
    def _get_recommendations(self) -> List[str]:
        """Generate recommendations based on analysis"""
        recommendations = []
        
        if len(self.password) < 12:
            recommendations.append("Use at least 12 characters for better security")
        
        if not re.search(r'[A-Z]', self.password):
            recommendations.append("Add uppercase letters (A-Z)")
        
        if not re.search(r'[a-z]', self.password):
            recommendations.append("Add lowercase letters (a-z)")
        
        if not re.search(r'[0-9]', self.password):
            recommendations.append("Add numbers (0-9)")
        
        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'\",.>?/\\|`~]', self.password):
            recommendations.append("Add special characters (!@#$%^&*)")
        
        if not recommendations:
            recommendations.append("Great password! Consider changing it periodically.")
        
        return recommendations


# Example usage (for testing)
if __name__ == "__main__":
    test_passwords = [
        "password",
        "Pass123",
        "MyStr0ng!Pass",
        "qwerty123",
        "SecureP@ssw0rd2024!"
    ]
    
    for pwd in test_passwords:
        analyzer = PasswordAnalyzer(pwd)
        result = analyzer.analyze()
        print(f"\n{'='*50}")
        print(f"Password Score: {result['score']}/100")
        print(f"Strength: {result['strength']}")
        print(f"Feedback:")
        for item in result['feedback']:
            print(f"  {item}")
        print(f"Recommendations:")
        for i, rec in enumerate(result['recommendations'], 1):
            print(f"  {i}. {rec}")
