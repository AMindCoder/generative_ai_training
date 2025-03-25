"""
Example script demonstrating how to use the simplified Markdown to PDF converter
"""

import os
import sys
from md_to_pdf_converter import md_to_pdf, batch_convert

def main():
    # Example 1: Convert a single Markdown file to PDF
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sample_md_file = os.path.join(os.path.dirname(current_dir), "RAG", "Training_Plan_Pankaj_Chopra.md")
    
    if os.path.exists(sample_md_file):
        print(f"Converting {sample_md_file} to PDF...")
        output_pdf = md_to_pdf(sample_md_file)
        print(f"PDF created at: {output_pdf}")
    else:
        print(f"Sample file {sample_md_file} not found.")
        
    # Example 2: Convert all Markdown files in a directory
    markdown_dir = os.path.join(os.path.dirname(current_dir), "RAG")
    if os.path.exists(markdown_dir):
        print(f"\nConverting all Markdown files in {markdown_dir}...")
        pdf_files = batch_convert(markdown_dir)
        print(f"Created {len(pdf_files)} PDF files:")
        for pdf_file in pdf_files:
            print(f"  - {pdf_file}")
    else:
        print(f"Directory {markdown_dir} not found.")

if __name__ == "__main__":
    main()
