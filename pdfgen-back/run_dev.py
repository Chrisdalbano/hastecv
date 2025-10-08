"""
Development runner for Flask backend.
Sets environment variables and starts the Flask app in development mode.
"""
import os
import sys

# Set environment variables for development
os.environ['FLASK_ENV'] = 'development'
os.environ['FLASK_DEBUG'] = 'True'

# Import and run the Flask app
from app import app

if __name__ == "__main__":
    print("\n" + "="*60)
    print("  HasteCV Backend - Development Mode")
    print("="*60)
    print(f"  Environment: {os.environ.get('FLASK_ENV')}")
    print(f"  Debug: {os.environ.get('FLASK_DEBUG')}")
    print(f"  CORS Allowed: http://localhost:5173, http://127.0.0.1:5173")
    print("="*60 + "\n")
    
    app.run(debug=True, host='127.0.0.1', port=5000)

