# 🔐 Password Strength Analyzer

A comprehensive web application that analyzes password strength and provides security recommendations. Perfect for learning cybersecurity basics and web development.

## 📋 Features

✅ **Real-time Password Analysis**
- Analyzes password length, character types, and patterns
- Provides instant feedback with visual indicators
- Score calculation from 0-100

✅ **Security Checks**
- Detects common passwords
- Identifies keyboard patterns (qwerty, asdfgh, etc.)
- Warns about repeated characters
- Requires uppercase, lowercase, numbers, and special characters

✅ **User-Friendly Interface**
- Beautiful gradient design
- Real-time visual feedback with color-coded strength meter
- Password visibility toggle
- Clear recommendations for improvement

✅ **Security Tips**
- Do's and Don'ts for creating strong passwords
- Best practices for password management

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/cvalenzona/password-analyzer.git
   cd password-analyzer
   ```

2. **Create virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   - Navigate to `http://localhost:5000`
   - Start analyzing passwords!

## 📁 Project Structure

```
password-analyzer/
├── checker.py              # Core password analysis logic
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── tests.py               # Unit tests
├── templates/
│   └── index.html         # Web interface
├── static/
│   └── style.css          # Styling
└── README.md              # This file
```

## 🔧 How It Works

### Password Scoring Algorithm

The analyzer checks multiple criteria and assigns points:

| Check | Points | Details |
|-------|--------|----------|
| Length 8-12 chars | +20 | Minimum recommended length |
| Length 12+ chars | +25 | Excellent length |
| Uppercase letters | +15 | Contains A-Z |
| Lowercase letters | +15 | Contains a-z |
| Numbers | +15 | Contains 0-9 |
| Special characters | +20 | Contains !@#$%^&* etc |
| Not common password | Base score | Deducts -10 if common |
| No keyboard patterns | Base score | Deducts -10 if detected |
| No repeated chars | Base score | Deducts -5 if excessive |

**Total Maximum Score: 100+**

### Strength Levels

- **Very Weak**: 0-20 points (🔴 Red)
- **Weak**: 21-40 points (🟠 Orange)
- **Fair**: 41-60 points (🟡 Yellow)
- **Good**: 61-80 points (🟢 Teal)
- **Strong**: 81+ points (✅ Green)

## 🧪 Running Tests

Run unit tests to verify functionality:

```bash
python -m unittest tests.py
```

Test Coverage:
- Empty password handling
- Character type detection
- Keyboard pattern detection
- Common password detection
- Repeated character detection
- Score range validation
- Recommendation generation

## 📚 Learning Outcomes

This project teaches:

### Security Concepts
- ✅ Password complexity requirements
- ✅ Common password vulnerabilities
- ✅ Pattern recognition in security
- ✅ OWASP password guidelines

### Python Skills
- ✅ Object-oriented programming
- ✅ Regular expressions for pattern matching
- ✅ Unit testing
- ✅ Type hints and documentation

### Web Development
- ✅ Flask framework basics
- ✅ REST API design
- ✅ Frontend/Backend communication
- ✅ Responsive CSS design
- ✅ Fetch API and async JavaScript

## 🎓 Cybersecurity Concepts Covered

1. **Authentication Security**
   - Why strong passwords matter
   - Password requirements and standards

2. **Threat Analysis**
   - Common attack patterns
   - Dictionary attacks
   - Brute force considerations

3. **Input Validation**
   - Sanitization and validation
   - Pattern recognition

4. **Best Practices**
   - Password managers
   - Multi-factor authentication
   - Regular password changes

## 🔐 Security Notes

⚠️ **Important**: This is an educational tool. In production:
- Never send actual passwords to external services
- Use HTTPS for all communications
- Implement rate limiting to prevent brute force
- Add CSRF protection
- Use secure session management
- Never store passwords in logs

## 📝 Example Test Cases

```python
# Very Weak Password
analyzer = PasswordAnalyzer("password")
result = analyzer.analyze()
# Score: ~10-20, Strength: "Very Weak"

# Medium Password
analyzer = PasswordAnalyzer("Pass123")
result = analyzer.analyze()
# Score: ~50-60, Strength: "Fair"

# Strong Password
analyzer = PasswordAnalyzer("SecureP@ssw0rd2024!")
result = analyzer.analyze()
# Score: ~85-95, Strength: "Strong"
```

## 🌟 Enhancement Ideas

Consider adding these features to expand your portfolio:

1. **Password Generation**
   - Generate strong random passwords
   - Customizable criteria

2. **Password History**
   - Store analysis history (encrypted)
   - Track improvement over time

3. **Database Integration**
   - SQLite/PostgreSQL for persistent storage
   - User accounts and authentication

4. **API Improvements**
   - Rate limiting
   - Authentication tokens
   - Error handling

5. **Advanced Checks**
   - Breach database lookup (Have I Been Pwned API)
   - Context-based recommendations
   - Language-specific patterns

6. **Deployment**
   - Docker containerization
   - Deploy to Heroku/AWS/DigitalOcean
   - CI/CD pipeline setup

## 📦 Dependencies

- **Flask 2.3.3**: Web framework
- **Werkzeug 2.3.7**: WSGI utilities and security

## 📄 License

MIT License - Feel free to use this project for learning and portfolio building!

## 🤝 Contributing

Feel free to fork, modify, and enhance this project. Some contribution ideas:
- Internationalization (i18n)
- Additional language support
- More security checks
- Performance optimizations
- UI/UX improvements

## 📞 Support

Have questions? Check the code comments or reach out!

---

**Happy Learning! 🚀**

*Building security skills one password at a time.*
