"""
Password Strength Analyzer - Flask Web Application
Provides a web interface for password analysis
"""

from flask import Flask, render_template, request, jsonify
from checker import PasswordAnalyzer
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """API endpoint to analyze password"""
    try:
        data = request.get_json()
        password = data.get('password', '')
        
        if not password:
            return jsonify({
                'error': 'Password is required',
                'success': False
            }), 400
        
        # Analyze password
        analyzer = PasswordAnalyzer(password)
        result = analyzer.analyze()
        
        # Determine color based on strength
        strength_colors = {
            'Very Weak': '#dc3545',  # Red
            'Weak': '#fd7e14',        # Orange
            'Fair': '#ffc107',        # Yellow
            'Good': '#20c997',        # Teal
            'Strong': '#28a745'       # Green
        }
        
        result['color'] = strength_colors.get(result['strength'], '#6c757d')
        result['success'] = True
        
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
