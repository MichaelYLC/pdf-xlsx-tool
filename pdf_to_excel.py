#!/usr/bin/env python3
"""
PDF to Excel Converter - CLI entry (repository root).
"""

import sys
from pathlib import Path

_root = Path(__file__).resolve().parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from pdf_xlsx_tool.converter import main

if __name__ == "__main__":
    main()
