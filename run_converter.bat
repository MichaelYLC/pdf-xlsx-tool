@echo off
echo ========================================
echo PDF to Excel Converter - Windows Launcher
echo ========================================
echo.

REM Check if executable exists
if not exist "PDF_to_Excel_Converter.exe" (
    echo ERROR: PDF_to_Excel_Converter.exe not found!
    echo Please make sure the executable is in the same folder as this batch file.
    pause
    exit /b 1
)

echo PDF to Excel Converter found!
echo.

REM Get PDF file from user
set /p PDF_FILE="Enter the path to your PDF file: "

REM Check if PDF file exists
if not exist "%PDF_FILE%" (
    echo ERROR: PDF file not found: %PDF_FILE%
    pause
    exit /b 1
)

echo.
echo Available languages:
echo   zh - Chinese (default)
echo   en - English
echo   hi - Hindi
echo   th - Thai
echo   vi - Vietnamese
echo.

set /p LANGUAGE="Enter language code (or press Enter for Chinese): "

REM Set default language if empty
if "%LANGUAGE%"=="" set LANGUAGE=zh

echo.
echo Converting PDF to Excel...
echo File: %PDF_FILE%
echo Language: %LANGUAGE%
echo.

REM Run the converter
PDF_to_Excel_Converter.exe "%PDF_FILE%" -l %LANGUAGE%

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo Conversion completed successfully!
    echo ========================================
    echo.
    echo The Excel file has been created in the same folder as your PDF.
    echo.
    pause
) else (
    echo.
    echo ========================================
    echo Conversion failed!
    echo ========================================
    echo.
    echo Please check the error messages above.
    echo.
    pause
)
