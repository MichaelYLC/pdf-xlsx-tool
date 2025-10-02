# PDF to Excel Converter - PowerShell Launcher
# This script provides a more user-friendly interface for Windows users

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "PDF to Excel Converter - PowerShell Launcher" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if executable exists
if (-not (Test-Path "PDF_to_Excel_Converter.exe")) {
    Write-Host "ERROR: PDF_to_Excel_Converter.exe not found!" -ForegroundColor Red
    Write-Host "Please make sure the executable is in the same folder as this script." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "PDF to Excel Converter found!" -ForegroundColor Green
Write-Host ""

# Get PDF file from user
$pdfFile = Read-Host "Enter the path to your PDF file"

# Check if PDF file exists
if (-not (Test-Path $pdfFile)) {
    Write-Host "ERROR: PDF file not found: $pdfFile" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Available languages:" -ForegroundColor Yellow
Write-Host "  zh - Chinese (default)" -ForegroundColor White
Write-Host "  en - English" -ForegroundColor White
Write-Host "  hi - Hindi" -ForegroundColor White
Write-Host "  th - Thai" -ForegroundColor White
Write-Host "  vi - Vietnamese" -ForegroundColor White
Write-Host ""

$language = Read-Host "Enter language code (or press Enter for Chinese)"

# Set default language if empty
if ([string]::IsNullOrEmpty($language)) {
    $language = "zh"
}

Write-Host ""
Write-Host "Converting PDF to Excel..." -ForegroundColor Yellow
Write-Host "File: $pdfFile" -ForegroundColor White
Write-Host "Language: $language" -ForegroundColor White
Write-Host ""

# Run the converter
try {
    & ".\PDF_to_Excel_Converter.exe" $pdfFile -l $language
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Green
        Write-Host "Conversion completed successfully!" -ForegroundColor Green
        Write-Host "========================================" -ForegroundColor Green
        Write-Host ""
        Write-Host "The Excel file has been created in the same folder as your PDF." -ForegroundColor White
        Write-Host ""
        
        # Ask if user wants to open the Excel file
        $openFile = Read-Host "Would you like to open the Excel file? (y/n)"
        if ($openFile -eq "y" -or $openFile -eq "Y") {
            $excelFile = $pdfFile -replace '\.pdf$', "_converted_$language.xlsx"
            if (Test-Path $excelFile) {
                Start-Process $excelFile
            }
        }
    } else {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Red
        Write-Host "Conversion failed!" -ForegroundColor Red
        Write-Host "========================================" -ForegroundColor Red
        Write-Host ""
        Write-Host "Please check the error messages above." -ForegroundColor White
    }
} catch {
    Write-Host "An error occurred: $($_.Exception.Message)" -ForegroundColor Red
}

Write-Host ""
Read-Host "Press Enter to exit"
