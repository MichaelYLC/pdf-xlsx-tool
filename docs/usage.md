# Enhanced PDF to Excel Converter - Usage Guide

## 🎯 **New Feature: Language Support**

The converter lets you choose which non-Chinese language column to fill from the bilingual PDF.

## 📋 **Available Languages**

- `zh` - Chinese (default)
- `en` - English  
- `id` - Indonesian
- `th` - Thai
- `vi` - Vietnamese

## 🚀 **Usage Examples**

### **1. Convert with Chinese (default):**
```bash
python3 pdf_to_excel.py your_file.pdf
```

### **2. Convert with English:**
```bash
python3 pdf_to_excel.py your_file.pdf -l en
```

### **3. Convert with Vietnamese:**
```bash
python3 pdf_to_excel.py your_file.pdf -l vi
```

### **4. Convert with Thai:**
```bash
python3 pdf_to_excel.py your_file.pdf -l th
```

### **5. Convert with Indonesian:**
```bash
python3 pdf_to_excel.py your_file.pdf -l id
```

### **6. Convert with custom output directory:**
```bash
python3 pdf_to_excel.py your_file.pdf -l en -o /path/to/output
```

### **7. Batch convert all PDFs with English:**
```bash
python3 pdf_to_excel.py . --batch -l en
```

## 📊 **What Happens with Each Language Option**

### **Chinese (zh) - Default:**
- Fills: 題目_zh, 選項A_zh, 選項B_zh, 選項C_zh, 選項D_zh
- Other language columns remain empty

### **English (en):**
- Fills: 題目_en, 選項A_en, 選項B_en, 選項C_en, 選項D_en
- Other language columns remain empty

### **Vietnamese (vi):**
- Fills: 題目_vi, 選項A_vi, 選項B_vi, 選項C_vi, 選項D_vi
- Other language columns remain empty

### **Thai (th):**
- Fills: 題目_th, 選項A_th, 選項B_th, 選項C_th, 選項D_th
- Other language columns remain empty

### **Indonesian (id):**
- Fills: 題目_id, 選項A_id, 選項B_id, 選項C_id, 選項D_id
- Other language columns remain empty

## 🎯 **Practical Examples**

### **For English-speaking users:**
```bash
python3 pdf_to_excel.py forklift_manual.pdf -l en
```
This creates `forklift_manual_converted_en.xlsx` with English columns filled.

### **For Vietnamese users:**
```bash
python3 pdf_to_excel.py forklift_manual.pdf -l vi
```
This creates `forklift_manual_converted_vi.xlsx` with Vietnamese columns filled.

### **For batch processing:**
```bash
python3 pdf_to_excel.py /path/to/pdfs --batch -l en
```
This converts all PDFs in the directory with English columns filled.

## 📁 **Output Files**

The converter creates files with language suffixes:
- `filename_converted.xlsx` (Chinese - default)
- `filename_converted_en.xlsx` (English)
- `filename_converted_vi.xlsx` (Vietnamese)
- `filename_converted_th.xlsx` (Thai)
- `filename_converted_id.xlsx` (Indonesian)

## ✅ **Benefits**

1. **Targeted Language Support** - Fill the language you need
2. **Consistent Format** - Same Excel structure for all languages
3. **Easy Translation** - Other language columns ready for manual translation
4. **Batch Processing** - Convert multiple files with same language setting
5. **Flexible Output** - Custom output directories supported

## 🔧 **Command Line Options**

- `input` - PDF file or directory containing PDF files
- `-o, --output` - Output directory (default: same as input)
- `--batch` - Process all PDF files in directory
- `-l, --lang` - Target language (zh, en, id, th, vi)
- `-h, --help` - Show help message

## 🎉 **Ready to Use!**

Choose the language option that matches the second language in your PDF.
