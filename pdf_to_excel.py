#!/usr/bin/env python3
"""
PDF to Excel Converter - Main Script
Converts PDF quiz files to Excel format with language support
"""

import sys
import os
from pathlib import Path

# Add the tools directory to the path
tools_dir = Path(__file__).parent / "pdf_converter_tools"
sys.path.insert(0, str(tools_dir))

# Import and run the enhanced converter
from enhanced_pdf_converter import main

if __name__ == "__main__":
    main()
