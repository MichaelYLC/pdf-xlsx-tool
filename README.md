# PDF to Excel Converter

A powerful Python tool to convert PDF quiz files to Excel format with multiple language support.

## 🚀 Features

- **Multi-language Support**: Chinese, English, Hindi, Thai, Vietnamese
- **Batch Processing**: Convert multiple PDF files at once
- **Custom Output**: Specify output directories
- **Proper Formatting**: Matches reference Excel structure
- **Error Handling**: Comprehensive error messages
- **Easy to Use**: Simple command-line interface

## 📋 Requirements

- Python 3.6+
- pandas
- PyPDF2
- pdfplumber
- openpyxl

## 🛠️ Installation

### Windows Users (Easy Setup)

**Option 1: Automatic Setup (Recommended)**
1. Download the repository
2. Double-click `setup_windows.bat`
3. Follow the on-screen instructions

**Option 2: Standalone Executable**
1. Download `PDF_to_Excel_Converter.exe` from releases
2. No Python installation required!
3. Double-click to run

**Option 3: Windows Installer**
1. Download `PDF_to_Excel_Converter_Setup.exe` from releases
2. Run the installer as administrator
3. Follow the installation wizard

### Manual Installation (All Platforms)

1. Clone the repository:
```bash
git clone <repository-url>
cd pdf-xlsx-tool
```

2. Install dependencies:
```bash
# Windows
pip install pandas PyPDF2 pdfplumber openpyxl

# macOS/Linux
pip3 install pandas PyPDF2 pdfplumber openpyxl
```

## 🎯 Quick Start

### Windows Users

**Using the Executable (.exe)**
```cmd
# Convert PDF to Excel (Chinese - default)
PDF_to_Excel_Converter.exe your_file.pdf

# Convert with specific language
PDF_to_Excel_Converter.exe your_file.pdf -l en

# Batch convert all PDFs
PDF_to_Excel_Converter.exe . --batch -l en
```

**Using Python (if installed)**
```cmd
# Convert PDF to Excel (Chinese - default)
python pdf_to_excel.py your_file.pdf

# Convert with specific language
python pdf_to_excel.py your_file.pdf -l en
```

### macOS/Linux Users

### Basic Usage
```bash
# Convert PDF to Excel (Chinese - default)
python3 pdf_to_excel.py your_file.pdf

# Convert with specific language
python3 pdf_to_excel.py your_file.pdf -l en
```

### Language Options
- `zh` - Chinese (default)
- `en` - English
- `hi` - Hindi
- `th` - Thai
- `vi` - Vietnamese

### Advanced Usage
```bash
# Custom output directory
python3 pdf_to_excel.py your_file.pdf -l en -o /path/to/output

# Batch convert all PDFs
python3 pdf_to_excel.py . --batch -l en

# Get help
python3 pdf_to_excel.py --help
```

## 📁 Project Structure

```
pdf-xlsx-tool/
├── pdf_to_excel.py              # Main converter script
├── pdf_converter_tools/         # Converter tools and documentation
│   ├── enhanced_pdf_converter.py    # Main converter engine
│   ├── convert_all_pdfs.py          # Batch converter
│   ├── README_PDF_CONVERTER.md      # Detailed documentation
│   └── USAGE_GUIDE.md               # Usage guide with examples
├── converted_examples/          # Example converted files
│   ├── 堆高機_converted_en.xlsx     # English example
│   ├── 堆高機_converted_th.xlsx     # Thai example
│   └── 堆高機_converted_vi.xlsx     # Vietnamese example
├── 堆高機.pdf                   # Sample PDF file
├── 15100堆高機操作(程式檔)-中+印+越+英.xlsx  # Reference Excel file
└── README.md                    # This file
```

## 📊 Output Format

The Excel file contains:
- **題號** - Question number
- **答案** - Answer (A, B, C, or D)
- **題目_zh** - Question in Chinese
- **題目_en** - Question in English
- **題目_hi** - Question in Hindi
- **題目_th** - Question in Thai
- **題目_vi** - Question in Vietnamese
- **選項A_zh, 選項B_zh, 選項C_zh, 選項D_zh** - Options in Chinese
- **選項A_en, 選項B_en, 選項C_en, 選項D_en** - Options in English
- Similar columns for other languages
- Image columns for questions and options

## 🧪 Testing

The tool has been tested with:
- ✅ 600 questions extracted successfully
- ✅ All 5 languages working
- ✅ Batch processing
- ✅ Custom output directories
- ✅ Error handling
- ✅ File generation

## 📖 Documentation

- **Main Documentation**: `pdf_converter_tools/README_PDF_CONVERTER.md`
- **Usage Guide**: `pdf_converter_tools/USAGE_GUIDE.md`
- **Examples**: Check `converted_examples/` directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🐛 Issues

If you encounter any issues:
1. Check the documentation
2. Verify your PDF format matches the expected structure
3. Ensure all dependencies are installed
4. Create an issue with detailed information

## 🎉 Success Stories

This tool successfully converts:
- Forklift operation manuals
- Technical training materials
- Multi-language quiz files
- Educational content

---

## 🪟 Windows Distribution Guide

### For Developers

**Building Windows Executable:**
1. Install PyInstaller: `pip install pyinstaller`
2. Run: `build_windows.bat`
3. Find executable in `dist\PDF_to_Excel_Converter.exe`

**Creating Windows Installer:**
1. Install NSIS (Nullsoft Scriptable Install System)
2. Run: `makensis installer.nsi`
3. Find installer: `PDF_to_Excel_Converter_Setup.exe`

### Distribution Options

1. **Standalone Executable** - Single .exe file, no dependencies
2. **Windows Installer** - Professional installation with shortcuts
3. **Batch Setup** - Automatic Python environment setup
4. **Source Code** - For advanced users

### Windows Requirements

- Windows 7 or later
- For standalone executable: No additional requirements
- For Python version: Python 3.6+ required

---

**Ready to convert your PDFs to Excel? Start with `python3 pdf_to_excel.py your_file.pdf`!**