"""
Simple Markdown to PDF Converter Utility

This module provides functions to convert Markdown files to PDF using the md2pdf library.
"""

import os
import logging
import subprocess
import time
from md2pdf.core import md2pdf

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def md_to_pdf(markdown_file, output_pdf=None, css_file=None):
    """
    Convert a Markdown file to PDF using md2pdf library.
    
    Args:
        markdown_file (str): Path to the Markdown file to convert
        output_pdf (str, optional): Path to save the output PDF. If None, uses the same name as the input file with .pdf extension
        css_file (str, optional): Path to a custom CSS file for styling the PDF
        
    Returns:
        str: Path to the generated PDF file
        
    Raises:
        FileNotFoundError: If the markdown file doesn't exist
        Exception: If there's an error during conversion
    """
    try:
        # Validate input file
        if not os.path.exists(markdown_file):
            raise FileNotFoundError(f"Markdown file not found: {markdown_file}")
        
        # Set default output path if not provided
        if output_pdf is None:
            output_pdf = os.path.splitext(markdown_file)[0] + '.pdf'
            
        # Set default CSS if not provided
        if css_file is None:
            # Create a default CSS with good styling for Markdown
            default_css = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'default.css')
            if not os.path.exists(default_css):
                with open(default_css, 'w') as f:
                    f.write("""
                    body {
                        font-family: Arial, sans-serif;
                        line-height: 1.5;
                        margin: 20px;
                        color: #333;
                    }
                    h1, h2, h3, h4, h5, h6 {
                        color: #0047AB;
                        margin-top: 20px;
                        margin-bottom: 10px;
                    }
                    h1 { font-size: 24px; }
                    h2 { font-size: 20px; }
                    h3 { font-size: 18px; }
                    h4 { font-size: 16px; }
                    h5 { font-size: 14px; }
                    h6 { font-size: 12px; }
                    p {
                        margin: 10px 0;
                    }
                    ul, ol {
                        margin: 10px 0;
                        padding-left: 30px;
                    }
                    li {
                        margin: 5px 0;
                    }
                    code {
                        background-color: #f5f5f5;
                        border: 1px solid #ddd;
                        border-radius: 3px;
                        font-family: monospace;
                        padding: 2px 4px;
                    }
                    pre {
                        background-color: #f5f5f5;
                        border: 1px solid #ddd;
                        border-radius: 3px;
                        padding: 10px;
                        overflow: auto;
                    }
                    blockquote {
                        border-left: 5px solid #ddd;
                        margin: 10px 0;
                        padding-left: 15px;
                        color: #666;
                    }
                    strong, b {
                        font-weight: bold;
                    }
                    em, i {
                        font-style: italic;
                    }
                    """)
            css_file = default_css
        
        # Handle file permission issues by trying with a different filename if the original is locked
        try:
            # Convert Markdown to PDF using md2pdf
            md2pdf(
                pdf_file_path=output_pdf,
                md_file_path=markdown_file,
                css_file_path=css_file
            )
        except PermissionError:
            # If the file is open or locked, try with a different filename
            alt_output_pdf = os.path.splitext(output_pdf)[0] + f"_{int(time.time())}.pdf"
            logger.info(f"Original PDF file is locked. Trying alternative filename: {alt_output_pdf}")
            
            md2pdf(
                pdf_file_path=alt_output_pdf,
                md_file_path=markdown_file,
                css_file_path=css_file
            )
            output_pdf = alt_output_pdf
        
        logger.info(f"Successfully converted {markdown_file} to {output_pdf}")
        return output_pdf
        
    except Exception as e:
        logger.error(f"Error converting Markdown to PDF: {str(e)}")
        raise

def batch_convert(markdown_dir, output_dir=None, css_file=None):
    """
    Convert all Markdown files in a directory to PDF.
    
    Args:
        markdown_dir (str): Directory containing Markdown files
        output_dir (str, optional): Directory to save PDF files. If None, PDFs are saved in the same directory as the Markdown files
        css_file (str, optional): Path to a custom CSS file for styling the PDFs
        
    Returns:
        list: Paths to all generated PDF files
        
    Raises:
        FileNotFoundError: If the markdown directory doesn't exist
    """
    if not os.path.isdir(markdown_dir):
        raise FileNotFoundError(f"Directory not found: {markdown_dir}")
    
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    pdf_files = []
    
    for filename in os.listdir(markdown_dir):
        if filename.lower().endswith('.md'):
            md_path = os.path.join(markdown_dir, filename)
            
            if output_dir:
                pdf_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.pdf')
            else:
                pdf_path = os.path.splitext(md_path)[0] + '.pdf'
                
            try:
                pdf_file = md_to_pdf(md_path, pdf_path, css_file)
                pdf_files.append(pdf_file)
            except Exception as e:
                logger.error(f"Error converting {md_path}: {str(e)}")
    
    return pdf_files

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Convert Markdown files to PDF")
    parser.add_argument("input", help="Input Markdown file or directory")
    parser.add_argument("-o", "--output", help="Output PDF file or directory")
    parser.add_argument("-c", "--css", help="Custom CSS file for styling")
    
    args = parser.parse_args()
    
    if os.path.isdir(args.input):
        batch_convert(args.input, args.output, args.css)
    else:
        md_to_pdf(args.input, args.output, args.css)
