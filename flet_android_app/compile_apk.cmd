@echo off
REM ===========================
REM Build Flet app into APK
REM ===========================

REM Set your main Python file
set MAIN_FILE=main.py

REM Step 1: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH!
    pause
    exit /b
)

REM Step 2: Install Flet (if missing)
pip show flet >nul 2>&1
if errorlevel 1 (
    echo Installing Flet...
    pip install flet
)

REM Step 3: Install build dependencies
pip install flet[all]

REM Step 4: Build APK
echo Building APK...
flet build apk %MAIN_FILE%

REM Step 5: Done
echo.
echo ===========================
echo APK build complete!
echo Check the "build" folder.
echo ===========================
pause