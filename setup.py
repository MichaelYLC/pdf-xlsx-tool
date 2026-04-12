#!/usr/bin/env python3
"""
Setup script for PDF to Excel Converter
Installs required dependencies
"""

import subprocess
import sys

def install_requirements():
    """Install required Python packages"""
    requirements = [
        'pdfplumber',
        'openpyxl',
    ]
    
    print("Installing required packages...")
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False
    
    print("\n🎉 All packages installed successfully!")
    print("\nYou can now use the PDF to Excel converter:")
    print("python3 pdf_to_excel.py your_file.pdf")
    return True

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version {sys.version.split()[0]} is compatible")
    return True

def main():
    print("🚀 PDF to Excel Converter Setup")
    print("=" * 40)
    
    if not check_python_version():
        sys.exit(1)
    
    if not install_requirements():
        sys.exit(1)
    
    print("\n📋 Setup complete! You can now:")
    print("1. Convert PDF files: python3 pdf_to_excel.py your_file.pdf")
    print("2. Use language options: python3 pdf_to_excel.py your_file.pdf -l en")
    print("3. Get help: python3 pdf_to_excel.py --help")

if __name__ == "__main__":
    main()
