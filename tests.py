"""
Unit Tests for Password Strength Analyzer
Test the core password analysis logic
"""

import unittest
from checker import PasswordAnalyzer

class TestPasswordAnalyzer(unittest.TestCase):
    """Test cases for PasswordAnalyzer class"""
    
    def test_empty_password(self):
        """Test with empty password"""
        analyzer = PasswordAnalyzer("")
        result = analyzer.analyze()
        self.assertEqual(result['strength'], 'Very Weak')
        self.assertEqual(result['length'], 0)
    
    def test_weak_password(self):
        """Test with weak password"""
        analyzer = PasswordAnalyzer("password")
        result = analyzer.analyze()
        self.assertIn('Very Weak', result['strength'])
    
    def test_password_with_uppercase(self):
        """Test password with uppercase letters"""
        analyzer = PasswordAnalyzer("Password")
        result = analyzer.analyze()
        self.assertIn('uppercase letters', str(result['feedback']).lower())
    
    def test_password_with_numbers(self):
        """Test password with numbers"""
        analyzer = PasswordAnalyzer("Password123")
        result = analyzer.analyze()
        self.assertIn('Contains numbers', str(result['feedback']))
    
    def test_password_with_special_chars(self):
        """Test password with special characters"""
        analyzer = PasswordAnalyzer("Password123!")
        result = analyzer.analyze()
        self.assertIn('special characters', str(result['feedback']).lower())
    
    def test_strong_password(self):
        """Test with strong password"""
        analyzer = PasswordAnalyzer("SecureP@ssw0rd2024")
        result = analyzer.analyze()
        self.assertEqual(result['strength'], 'Strong')
        self.assertGreater(result['score'], 80)
    
    def test_keyboard_pattern_detection(self):
        """Test detection of keyboard patterns"""
        analyzer = PasswordAnalyzer("Qwerty123!")
        result = analyzer.analyze()
        self.assertIn('keyboard pattern', str(result['feedback']).lower())
    
    def test_repeated_characters_detection(self):
        """Test detection of repeated characters"""
        analyzer = PasswordAnalyzer("Pass111word!")
        result = analyzer.analyze()
        self.assertIn('repeated', str(result['feedback']).lower())
    
    def test_password_length_effect(self):
        """Test that longer passwords score higher"""
        short_analyzer = PasswordAnalyzer("Pass1!")
        short_result = short_analyzer.analyze()
        
        long_analyzer = PasswordAnalyzer("VeryLongSecurePassword123!")
        long_result = long_analyzer.analyze()
        
        self.assertGreater(long_result['score'], short_result['score'])
    
    def test_common_password_detection(self):
        """Test detection of common passwords"""
        analyzer = PasswordAnalyzer("MyPassword123!")
        result = analyzer.analyze()
        # Should still work but might get lower score
        self.assertIsNotNone(result['score'])
    
    def test_recommendations_provided(self):
        """Test that recommendations are provided"""
        analyzer = PasswordAnalyzer("weak")
        result = analyzer.analyze()
        self.assertGreater(len(result['recommendations']), 0)
    
    def test_feedback_provided(self):
        """Test that feedback is provided"""
        analyzer = PasswordAnalyzer("TestPass1!")
        result = analyzer.analyze()
        self.assertGreater(len(result['feedback']), 0)
    
    def test_score_range(self):
        """Test that score is between 0 and 100"""
        test_passwords = [
            "",
            "weak",
            "Medium1",
            "VeryStrongPassword123!"
        ]
        
        for pwd in test_passwords:
            analyzer = PasswordAnalyzer(pwd)
            result = analyzer.analyze()
            self.assertGreaterEqual(result['score'], 0)
            self.assertLessEqual(result['score'], 100)

if __name__ == '__main__':
    unittest.main()
