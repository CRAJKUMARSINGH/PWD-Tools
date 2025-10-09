@echo off
title PWD Tools Hub - Main Application
echo ========================================
echo   PWD Tools Hub - Main Application
echo ========================================
echo.
echo Starting the PWD Tools Hub application...
echo.
echo The app will be available at: http://localhost:8501
echo.
echo For deployment instructions, see DEPLOYMENT.md
echo Streamlit Cloud deployment uses streamlit_app.py as entry point
echo.
echo Press Ctrl+C to stop the application
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and make sure it's accessible from the command line
    echo.
    echo For deployment options, see DEPLOYMENT.md
    echo.
    pause
    exit /b 1
)

REM Check if Streamlit is installed
python -c "import streamlit" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Streamlit...
    python -m pip install streamlit
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install Streamlit
        echo Please make sure you have pip installed and internet connection
        echo.
        echo For deployment options, see DEPLOYMENT.md
        echo.
        pause
        exit /b 1
    )
)

echo Starting PWD Tools Hub...
echo.
python -m streamlit run app.py

pause