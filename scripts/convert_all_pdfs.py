#!/usr/bin/env python3
"""Convert all PDF files in a directory to Excel (wrapper around the package API)."""

import argparse
import sys
from pathlib import Path

_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))

from pdf_xlsx_tool.converter import convert_single_pdf


def main():
    parser = argparse.ArgumentParser(description="Convert every *.pdf in a directory to Excel.")
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing PDF files (default: current directory)",
    )
    parser.add_argument("-o", "--output", help="Output directory (default: same folder as each PDF)")
    parser.add_argument(
        "-l",
        "--lang",
        choices=["en", "id", "th", "vi"],
        help="Target language paired with Chinese in the PDF",
    )
    args = parser.parse_args()
    directory = Path(args.directory).resolve()
    if not directory.is_dir():
        print(f"Not a directory: {directory}")
        sys.exit(1)
    pdfs = sorted(directory.glob("*.pdf"))
    if not pdfs:
        print("No PDF files found.")
        return
    for pdf in pdfs:
        convert_single_pdf(pdf, args.output, args.lang)
    print(f"\nDone. Processed {len(pdfs)} file(s).")


if __name__ == "__main__":
    main()
