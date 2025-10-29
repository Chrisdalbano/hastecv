# Development server startup script for Windows PowerShell
# This ensures Flask runs in development mode with proper CORS settings

Write-Host "====================================" -ForegroundColor Cyan
Write-Host "Starting HasteCV Backend - DEV MODE" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Set environment variables
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG = "true"

Write-Host "Environment: $env:FLASK_ENV" -ForegroundColor Green
Write-Host "Debug Mode: $env:FLASK_DEBUG" -ForegroundColor Green
Write-Host ""
Write-Host "CORS enabled for localhost:5173" -ForegroundColor Yellow
Write-Host "Starting server on http://127.0.0.1:5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Run Flask app
python app.py

