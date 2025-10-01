# PDF to Excel Converter

This tool converts PDF quiz files to Excel format with multiple language support, matching the structure of your reference Excel file.

## Features

- Extracts quiz questions from PDF files
- Handles multi-line questions and options
- Creates Excel files with the same structure as your reference file
- Supports batch processing of multiple PDF files
- Includes columns for Chinese, English, Hindi, Thai, and Vietnamese translations
- Auto-adjusts column widths for better readability

## Files

- `comprehensive_pdf_to_excel_converter.py` - Main converter script
- `convert_all_pdfs.py` - Simple script to convert all PDFs in current directory
- `堆高機_converted_comprehensive.xlsx` - Example output file

## Usage

### Convert a single PDF file:
```bash
python3 comprehensive_pdf_to_excel_converter.py your_file.pdf
```

### Convert all PDF files in a directory:
```bash
python3 comprehensive_pdf_to_excel_converter.py /path/to/pdf/directory --batch
```

### Convert all PDF files in current directory:
```bash
python3 convert_all_pdfs.py
```

### Specify output directory:
```bash
python3 comprehensive_pdf_to_excel_converter.py your_file.pdf -o /path/to/output
```

## Output Format

The Excel file will have the following structure:
- **題號** - Question number
- **答案** - Answer (A, B, C, or D)
- **題目_zh** - Question text in Chinese
- **題目_en** - Question text in English (empty, for manual translation)
- **題目_hi** - Question text in Hindi (empty, for manual translation)
- **題目_th** - Question text in Thai (empty, for manual translation)
- **題目_vi** - Question text in Vietnamese (empty, for manual translation)
- **選項A_zh** - Option A in Chinese
- **選項A_en** - Option A in English (empty, for manual translation)
- **選項A_hi** - Option A in Hindi (empty, for manual translation)
- **選項A_th** - Option A in Thai (empty, for manual translation)
- **選項A_vi** - Option A in Vietnamese (empty, for manual translation)
- Similar columns for options B, C, and D
- Image columns for questions and options (empty, for manual addition)

## Next Steps After Conversion

1. **Open the Excel file** in your preferred spreadsheet application
2. **Fill in translations** for other languages (English, Hindi, Thai, Vietnamese)
3. **Add images** if needed in the image columns
4. **Review and adjust formatting** as necessary
5. **Save the file** when complete

## Requirements

- Python 3.6+
- pandas
- PyPDF2
- pdfplumber
- openpyxl

Install requirements:
```bash
pip3 install pandas PyPDF2 pdfplumber openpyxl
```

## Troubleshooting

- If questions are not extracted properly, check that the PDF contains text (not just images)
- The converter looks for questions in the format: "1. (4) Question text..."
- Options should be marked with Chinese numbers: ①, ②, ③, ④
- Make sure the PDF is not password-protected

## Example

Input PDF format:
```
1. (4) 有關消音器之敘述，下列何者錯誤？ ①以消音為主要功能，亦稱滅音器
②利用觸媒使一氧化碳變成二氧化碳 ③利用離心力使廢氣中碳粒分離 ④氣溫較低時，淨化效果更佳 。
```

Output Excel format:
- 題號: 1
- 答案: D
- 題目_zh: 有關消音器之敘述，下列何者錯誤？
- 選項A_zh: 以消音為主要功能，亦稱滅音器
- 選項B_zh: 利用觸媒使一氧化碳變成二氧化碳
- 選項C_zh: 利用離心力使廢氣中碳粒分離
- 選項D_zh: 氣溫較低時，淨化效果更佳
