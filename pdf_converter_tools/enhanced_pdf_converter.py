#!/usr/bin/env python3
"""
Enhanced PDF to Excel Converter with Language Support
Allows specifying which language column to fill automatically
"""

import pandas as pd
import pdfplumber
import openpyxl
from openpyxl import Workbook
import re
import sys
import os
from pathlib import Path
import argparse

class QuizQuestion:
    def __init__(self):
        self.question_number = ""
        self.answer = ""
        self.question_text = ""
        self.options = {"A": "", "B": "", "C": "", "D": ""}

def extract_quiz_questions_from_pdf(pdf_path):
    """Extract quiz questions from PDF with proper parsing"""
    questions = []
    
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n"
    
    # Split by question numbers to get individual questions
    question_pattern = r'(\d+)\.\s*\(([1-4])\)\s*(.+?)(?=\d+\.\s*\([1-4]\)|$)'
    question_matches = re.findall(question_pattern, full_text, re.DOTALL)
    
    for match in question_matches:
        question_number = match[0]
        answer_number = match[1]
        question_content = match[2].strip()
        
        # Create question object
        question = QuizQuestion()
        question.question_number = question_number
        answer_map = {"1": "A", "2": "B", "3": "C", "4": "D"}
        question.answer = answer_map[answer_number]
        
        # Process the question content
        process_question_content(question, question_content)
        questions.append(question)
    
    return questions

def process_question_content(question, content):
    """Process the question content to separate question text from options"""
    # Find the first option symbol
    first_option_pos = len(content)
    for symbol in ['①', '②', '③', '④']:
        pos = content.find(symbol)
        if pos != -1 and pos < first_option_pos:
            first_option_pos = pos
    
    if first_option_pos < len(content):
        # Separate question from options
        question.question_text = content[:first_option_pos].strip()
        options_content = content[first_option_pos:].strip()
        
        # Process options
        process_options(question, options_content)
    else:
        question.question_text = content

def process_options(question, options_content):
    """Process options content to extract individual options"""
    # Split by option symbols
    option_symbols = ['①', '②', '③', '④']
    option_map = {"①": "A", "②": "B", "③": "C", "④": "D"}
    
    # Find all option positions
    option_positions = []
    for symbol in option_symbols:
        pos = options_content.find(symbol)
        if pos != -1:
            option_positions.append((pos, symbol))
    
    # Sort by position
    option_positions.sort(key=lambda x: x[0])
    
    # Extract each option
    for i, (pos, symbol) in enumerate(option_positions):
        # Find the end position (next option or end of text)
        if i + 1 < len(option_positions):
            end_pos = option_positions[i + 1][0]
        else:
            end_pos = len(options_content)
        
        # Extract option text
        option_text = options_content[pos:end_pos].strip()
        # Remove the symbol from the beginning
        option_text = re.sub(r'^[①②③④]\s*', '', option_text).strip()
        
        if option_text:
            question.options[option_map[symbol]] = option_text

def create_excel_with_quiz_structure(questions, output_path, target_lang=None):
    """Create Excel file with the same structure as the reference file"""
    wb = Workbook()
    ws = wb.active
    ws.title = "converted"
    
    # Language mapping
    lang_columns = {
        'zh': {'question': 3, 'A': 8, 'B': 13, 'C': 18, 'D': 23},
        'en': {'question': 4, 'A': 9, 'B': 14, 'C': 19, 'D': 24},
        'hi': {'question': 5, 'A': 10, 'B': 15, 'C': 20, 'D': 25},
        'th': {'question': 6, 'A': 11, 'B': 16, 'C': 21, 'D': 26},
        'vi': {'question': 7, 'A': 12, 'B': 17, 'C': 22, 'D': 27}
    }
    
    # Headers matching the reference file structure
    headers = [
        '題號', '答案', '題目_zh', '題目_en', '題目_hi', '題目_th', '題目_vi',
        '選項A_zh', '選項A_en', '選項A_hi', '選項A_th', '選項A_vi',
        '選項B_zh', '選項B_en', '選項B_hi', '選項B_th', '選項B_vi',
        '選項C_zh', '選項C_en', '選項C_hi', '選項C_th', '選項C_vi',
        '選項D_zh', '選項D_en', '選項D_hi', '選項D_th', '選項D_vi',
        '題目圖片', '選項A_圖片', '選項B_圖片', '選項C_圖片', '選項D_圖片'
    ]
    
    # Set headers
    for col, header in enumerate(headers, 1):
        ws.cell(row=1, column=col, value=header)
    
    # Add question data
    for row, question in enumerate(questions, 2):
        ws.cell(row=row, column=1, value=question.question_number)  # 題號
        ws.cell(row=row, column=2, value=question.answer)  # 答案
        
        # Fill in the specified language or default to Chinese
        if target_lang and target_lang in lang_columns:
            # Fill the specified language
            ws.cell(row=row, column=lang_columns[target_lang]['question'], value=question.question_text)
            ws.cell(row=row, column=lang_columns[target_lang]['A'], value=question.options['A'])
            ws.cell(row=row, column=lang_columns[target_lang]['B'], value=question.options['B'])
            ws.cell(row=row, column=lang_columns[target_lang]['C'], value=question.options['C'])
            ws.cell(row=row, column=lang_columns[target_lang]['D'], value=question.options['D'])
        else:
            # Default: fill Chinese columns
            ws.cell(row=row, column=3, value=question.question_text)  # 題目_zh
            ws.cell(row=row, column=8, value=question.options['A'])  # 選項A_zh
            ws.cell(row=row, column=13, value=question.options['B'])  # 選項B_zh
            ws.cell(row=row, column=18, value=question.options['C'])  # 選項C_zh
            ws.cell(row=row, column=23, value=question.options['D'])  # 選項D_zh
    
    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if cell.value and len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min(max_length + 2, 50)
        ws.column_dimensions[column_letter].width = adjusted_width
    
    wb.save(output_path)
    print(f"Excel file created with {len(questions)} questions: {output_path}")
    if target_lang:
        print(f"Content filled in {target_lang.upper()} language columns")

def convert_single_pdf(pdf_path, output_dir=None, target_lang=None):
    """Convert a single PDF to Excel format"""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"PDF file not found: {pdf_path}")
        return None
    
    if output_dir is None:
        output_dir = pdf_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(exist_ok=True)
    
    print(f"Processing: {pdf_path.name}")
    if target_lang:
        print(f"Target language: {target_lang.upper()}")
    
    # Extract questions
    questions = extract_quiz_questions_from_pdf(pdf_path)
    if not questions:
        print(f"No questions found in {pdf_path}")
        return None
    
    # Create output filename
    lang_suffix = f"_{target_lang}" if target_lang else ""
    output_filename = pdf_path.stem + f"_converted{lang_suffix}.xlsx"
    output_path = output_dir / output_filename
    
    # Create Excel file
    create_excel_with_quiz_structure(questions, output_path, target_lang)
    return output_path

def main():
    parser = argparse.ArgumentParser(description='Convert PDF quiz files to Excel format with language support')
    parser.add_argument('input', help='PDF file or directory containing PDF files')
    parser.add_argument('-o', '--output', help='Output directory (default: same as input)')
    parser.add_argument('--batch', action='store_true', help='Process all PDF files in directory')
    parser.add_argument('-l', '--lang', choices=['zh', 'en', 'hi', 'th', 'vi'], 
                       help='Target language to fill (zh=Chinese, en=English, hi=Hindi, th=Thai, vi=Vietnamese)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    
    if args.batch or input_path.is_dir():
        print("=== Batch Processing PDF Files ===")
        if input_path.is_dir():
            pdf_files = list(input_path.glob("*.pdf"))
            for pdf_file in pdf_files:
                convert_single_pdf(pdf_file, args.output, args.lang)
        else:
            print("Directory not found")
    else:
        print("=== Converting Single PDF File ===")
        output_path = convert_single_pdf(input_path, args.output, args.lang)
        if output_path:
            print(f"\n=== Conversion Complete ===")
            print(f"Output file: {output_path}")
            print("\nNext steps:")
            print("1. Open the Excel file")
            print("2. Fill in translations for other languages if needed")
            print("3. Add images if needed")
            print("4. Review and adjust formatting")

if __name__ == "__main__":
    # If no command line arguments, run with default files
    if len(sys.argv) == 1:
        pdf_path = "/Users/michael/Desktop/Projects/PracticePro/堆高機.pdf"
        output_path = "/Users/michael/Desktop/Projects/PracticePro/堆高機_converted_enhanced.xlsx"
        
        print("=== Converting Default PDF File ===")
        questions = extract_quiz_questions_from_pdf(pdf_path)
        
        if questions:
            print(f"Found {len(questions)} questions")
            
            # Show first few questions as preview
            for i, q in enumerate(questions[:3]):
                print(f"\nQuestion {q.question_number}:")
                print(f"  Answer: {q.answer}")
                print(f"  Text: {q.question_text}")
                print(f"  Options:")
                for opt, text in q.options.items():
                    if text:
                        print(f"    {opt}: {text}")
            
            create_excel_with_quiz_structure(questions, output_path)
            print(f"Output file: {output_path}")
        else:
            print("No questions found in the PDF")
    else:
        main()
