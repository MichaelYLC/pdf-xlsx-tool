@echo off
echo ========================================
echo Building PDF to Excel Converter for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Installing PyInstaller...
python -m pip install pyinstaller

if %errorlevel% neq 0 (
    echo ERROR: Failed to install PyInstaller
    pause
    exit /b 1
)

echo.
echo Building executable...
pyinstaller pdf_converter.spec

if %errorlevel% neq 0 (
    echo ERROR: Failed to build executable
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo The executable is located in: dist\PDF_to_Excel_Converter.exe
echo.
echo You can now distribute this single .exe file to Windows users.
echo They won't need Python installed to run it.
echo.
pause
