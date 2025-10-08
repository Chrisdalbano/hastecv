@echo off
echo ================================================
echo   HasteCV - Local Development Environment
echo ================================================
echo.

REM Check if node_modules exists in frontend
if not exist "pdfgen-front\node_modules\" (
    echo [SETUP] Installing frontend dependencies...
    cd pdfgen-front
    call npm install
    cd ..
    echo.
)

REM Check if Python virtual environment exists
if not exist "pdfgen-back\venv\" (
    echo [SETUP] Creating Python virtual environment...
    cd pdfgen-back
    python -m venv venv
    call venv\Scripts\activate
    echo [SETUP] Installing backend dependencies...
    pip install -r requirements.txt
    cd ..
    echo.
)

echo [STARTING] Launching HasteCV Development Servers...
echo.
echo [FRONTEND] Starting Vue.js development server on http://localhost:5173
echo [BACKEND] Starting Flask development server on http://localhost:5000
echo.
echo Press Ctrl+C to stop all servers
echo ================================================
echo.

REM Start backend in new window using the development runner
start "HasteCV Backend - Flask" cmd /k "cd pdfgen-back && venv\Scripts\activate && python run_dev.py"

REM Wait a moment for backend to start
timeout /t 3 /nobreak >nul

REM Start frontend in new window
start "HasteCV Frontend - Vite" cmd /k "cd pdfgen-front && npm run dev"

echo.
echo [SUCCESS] Both servers are starting in separate windows!
echo.
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:5000
echo.
echo Close this window or the individual server windows to stop the servers.
pause

