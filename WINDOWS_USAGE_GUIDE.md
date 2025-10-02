# How to Use the Windows Executable

## 🪟 **For Windows Users - Complete Guide**

### **Step 1: Download the Executable**

1. **Go to GitHub Releases:** https://github.com/MichaelYLC/pdf-xlsx-tool/releases
2. **Download:** `PDF_to_Excel_Converter.exe` (about 50MB)
3. **Save it** to your desired folder (e.g., Desktop, Documents)

### **Step 2: Run the Executable**

#### **Method 1: Command Prompt (Recommended)**

1. **Open Command Prompt:**
   - Press `Windows + R`
   - Type `cmd` and press Enter
   - Or search "Command Prompt" in Start menu

2. **Navigate to the executable:**
   ```cmd
   cd C:\Users\YourName\Desktop
   ```

3. **Run the converter:**
   ```cmd
   PDF_to_Excel_Converter.exe your_file.pdf
   ```

#### **Method 2: PowerShell**

1. **Open PowerShell:**
   - Press `Windows + X`
   - Select "Windows PowerShell"
   - Or search "PowerShell" in Start menu

2. **Navigate and run:**
   ```powershell
   cd C:\Users\YourName\Desktop
   .\PDF_to_Excel_Converter.exe your_file.pdf
   ```

#### **Method 3: File Explorer (Drag & Drop)**

1. **Open File Explorer**
2. **Navigate to your PDF file**
3. **Drag the PDF file** onto `PDF_to_Excel_Converter.exe`
4. **The conversion will start automatically**

### **Step 3: Command Examples**

#### **Basic Usage:**
```cmd
# Convert PDF to Excel (Chinese - default)
PDF_to_Excel_Converter.exe your_file.pdf

# Convert with specific language
PDF_to_Excel_Converter.exe your_file.pdf -l en

# Convert with English language
PDF_to_Excel_Converter.exe your_file.pdf -l en

# Convert with Hindi language
PDF_to_Excel_Converter.exe your_file.pdf -l hi

# Convert with Thai language
PDF_to_Excel_Converter.exe your_file.pdf -l th

# Convert with Vietnamese language
PDF_to_Excel_Converter.exe your_file.pdf -l vi
```

#### **Advanced Usage:**
```cmd
# Batch convert all PDFs in current folder
PDF_to_Excel_Converter.exe . --batch -l en

# Convert with custom output directory
PDF_to_Excel_Converter.exe your_file.pdf -l en -o C:\Output

# Get help
PDF_to_Excel_Converter.exe --help
```

### **Step 4: Language Options**

| Code | Language | Example |
|------|----------|---------|
| `zh` | Chinese (default) | `-l zh` |
| `en` | English | `-l en` |
| `hi` | Hindi | `-l hi` |
| `th` | Thai | `-l th` |
| `vi` | Vietnamese | `-l vi` |

### **Step 5: Output Files**

After conversion, you'll get:
- **Excel file:** `your_file_converted_en.xlsx` (or other language)
- **Location:** Same folder as your PDF file
- **Format:** Excel format with all question data

### **Step 6: Troubleshooting**

#### **Common Issues:**

**Issue: "Windows protected your PC"**
- **Solution:** Click "More info" → "Run anyway"
- **Or:** Right-click → "Properties" → "Unblock" → "OK"

**Issue: "Antivirus blocking"**
- **Solution:** Add exception in antivirus settings
- **Or:** Temporarily disable real-time protection

**Issue: "File not found"**
- **Solution:** Check file path and ensure PDF exists
- **Use:** Full path like `C:\Users\YourName\Desktop\file.pdf`

**Issue: "Permission denied"**
- **Solution:** Run Command Prompt as Administrator
- **Or:** Move files to a folder you have write access to

#### **Error Messages:**

```
Error: PDF file not found
→ Check the file path and name

Error: Invalid language code
→ Use: zh, en, hi, th, or vi

Error: Output directory not writable
→ Choose a different output location
```

### **Step 7: Performance Tips**

- **Large files:** May take 1-5 minutes to process
- **Memory:** Close other applications for large PDFs
- **Storage:** Ensure 100MB+ free space
- **CPU:** Process will use available CPU cores

### **Step 8: Example Workflow**

```cmd
# 1. Download PDF_to_Excel_Converter.exe to Desktop
# 2. Open Command Prompt
# 3. Navigate to Desktop
cd C:\Users\YourName\Desktop

# 4. Convert your PDF
PDF_to_Excel_Converter.exe my_quiz.pdf -l en

# 5. Check output
dir *.xlsx

# 6. Open the Excel file
start my_quiz_converted_en.xlsx
```

### **Step 9: Batch Processing**

To convert multiple PDFs at once:

```cmd
# Put all PDFs in one folder
# Run batch conversion
PDF_to_Excel_Converter.exe . --batch -l en

# This will convert ALL PDFs in the current folder
# Each will get its own Excel file
```

### **Step 10: Success Indicators**

✅ **Successful conversion shows:**
```
=== Converting Single PDF File ===
Processing: your_file.pdf
Target language: EN
Excel file created with 600 questions: your_file_converted_en.xlsx
Content filled in EN language columns

=== Conversion Complete ===
Output file: your_file_converted_en.xlsx
```

❌ **If you see errors:**
- Check the error message
- Verify file paths
- Ensure PDF is not corrupted
- Try a different output location

---

## 🎯 **Quick Start for Windows Users**

1. **Download** `PDF_to_Excel_Converter.exe` from GitHub
2. **Open Command Prompt**
3. **Navigate** to the executable location
4. **Run:** `PDF_to_Excel_Converter.exe your_file.pdf -l en`
5. **Open** the generated Excel file

**That's it! No Python installation needed!** 🚀
