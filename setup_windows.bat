@echo off
echo ========================================
echo PDF to Excel Converter - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.6+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Checking version...
python --version

REM Check Python version (basic check)
python -c "import sys; exit(0 if sys.version_info >= (3, 6) else 1)" >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python 3.6 or higher is required
    echo Please upgrade your Python installation
    pause
    exit /b 1
)

echo Python version is compatible!
echo.

REM Install required packages
echo Installing required packages...
echo.

python -m pip install --upgrade pip
python -m pip install pandas PyPDF2 pdfplumber openpyxl

if %errorlevel% neq 0 (
    echo ERROR: Failed to install required packages
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo You can now use the PDF to Excel converter:
echo.
echo Basic usage:
echo   python pdf_to_excel.py your_file.pdf
echo.
echo With language option:
echo   python pdf_to_excel.py your_file.pdf -l en
echo.
echo Batch convert all PDFs:
echo   python pdf_to_excel.py . --batch -l en
echo.
echo Get help:
echo   python pdf_to_excel.py --help
echo.
echo Press any key to exit...
pause >nul
