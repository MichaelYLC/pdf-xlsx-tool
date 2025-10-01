#!/usr/bin/env python3
"""
Simple script to convert all PDF files in the current directory to Excel format
"""

import os
import sys
from pathlib import Path
from comprehensive_pdf_to_excel_converter import convert_multiple_pdfs

def main():
    current_dir = Path.cwd()
    print(f"Converting all PDF files in: {current_dir}")
    
    converted_files = convert_multiple_pdfs(current_dir)
    
    if converted_files:
        print(f"\n=== Conversion Complete ===")
        print(f"Successfully converted {len(converted_files)} files:")
        for file_path in converted_files:
            print(f"  ✓ {file_path.name}")
        
        print(f"\nNext steps for each file:")
        print("1. Open the Excel file")
        print("2. Fill in translations for other languages (English, Hindi, Thai, Vietnamese)")
        print("3. Add images if needed")
        print("4. Review and adjust formatting")
    else:
        print("No PDF files found to convert")

if __name__ == "__main__":
    main()
