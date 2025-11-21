"""
Markdown to DOCX Converter Utility

This module provides functions to convert Markdown files to DOCX (Microsoft Word) format,
which can be easily imported and edited in Google Docs.
"""

import os
import logging
from pathlib import Path
import pypandoc

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def ensure_pandoc_installed():
    """
    Check if pandoc is installed, and provide installation instructions if not.

    Returns:
        bool: True if pandoc is available, False otherwise
    """
    try:
        pypandoc.get_pandoc_version()
        return True
    except OSError:
        logger.error("Pandoc is not installed. Please install it:")
        logger.error("  - macOS: brew install pandoc")
        logger.error("  - Linux: sudo apt-get install pandoc")
        logger.error("  - Windows: Download from https://pandoc.org/installing.html")
        logger.error("  - Or use: pypandoc.download_pandoc()")
        return False

def md_to_docx(markdown_file, output_docx=None, extra_args=None):
    """
    Convert a Markdown file to DOCX (Microsoft Word) format.
    The DOCX file can be directly uploaded to Google Docs.

    Args:
        markdown_file (str): Path to the Markdown file to convert
        output_docx (str, optional): Path to save the output DOCX. If None, uses the same name as the input file with .docx extension
        extra_args (list, optional): Additional arguments to pass to pandoc

    Returns:
        str: Path to the generated DOCX file

    Raises:
        FileNotFoundError: If the markdown file doesn't exist
        Exception: If there's an error during conversion
    """
    try:
        # Check if pandoc is installed
        if not ensure_pandoc_installed():
            raise RuntimeError("Pandoc is not installed. Cannot convert Markdown to DOCX.")

        # Validate input file
        if not os.path.exists(markdown_file):
            raise FileNotFoundError(f"Markdown file not found: {markdown_file}")

        # Set default output path if not provided
        if output_docx is None:
            output_docx = os.path.splitext(markdown_file)[0] + '.docx'

        # Set default pandoc arguments for better formatting
        if extra_args is None:
            extra_args = [
                '--standalone',  # Create a standalone document
                '--syntax-highlighting=pygments',  # Syntax highlighting for code blocks
                '--preserve-tabs',  # Preserve tab characters
                '--wrap=preserve',  # Preserve line wrapping
                '--reference-doc=None',  # Use default styling
            ]

        logger.info(f"Converting {markdown_file} to {output_docx}...")

        # Convert Markdown to DOCX using pypandoc
        pypandoc.convert_file(
            markdown_file,
            'docx',
            outputfile=output_docx,
            extra_args=extra_args
        )

        logger.info(f"Successfully converted {markdown_file} to {output_docx}")
        logger.info("You can now upload this DOCX file to Google Docs:")
        logger.info("  1. Go to https://docs.google.com")
        logger.info("  2. Click 'File' -> 'Open' -> 'Upload'")
        logger.info(f"  3. Select {output_docx}")

        return output_docx

    except Exception as e:
        logger.error(f"Error converting Markdown to DOCX: {str(e)}")
        raise

def batch_convert(markdown_dir, output_dir=None, extra_args=None):
    """
    Convert all Markdown files in a directory to DOCX.

    Args:
        markdown_dir (str): Directory containing Markdown files
        output_dir (str, optional): Directory to save DOCX files. If None, DOCX files are saved in the same directory as the Markdown files
        extra_args (list, optional): Additional arguments to pass to pandoc

    Returns:
        list: Paths to all generated DOCX files

    Raises:
        FileNotFoundError: If the markdown directory doesn't exist
    """
    if not os.path.isdir(markdown_dir):
        raise FileNotFoundError(f"Directory not found: {markdown_dir}")

    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    docx_files = []

    for filename in os.listdir(markdown_dir):
        if filename.lower().endswith('.md'):
            md_path = os.path.join(markdown_dir, filename)

            if output_dir:
                docx_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.docx')
            else:
                docx_path = os.path.splitext(md_path)[0] + '.docx'

            try:
                docx_file = md_to_docx(md_path, docx_path, extra_args)
                docx_files.append(docx_file)
            except Exception as e:
                logger.error(f"Error converting {md_path}: {str(e)}")

    logger.info(f"Converted {len(docx_files)} Markdown files to DOCX")
    return docx_files

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert Markdown files to DOCX format for Google Docs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert a single file
  python md_to_doc_converter.py input.md

  # Convert with custom output path
  python md_to_doc_converter.py input.md -o output.docx

  # Convert all MD files in a directory
  python md_to_doc_converter.py ./markdown_files/ -o ./docx_files/

  # Convert without table of contents
  python md_to_doc_converter.py input.md --no-toc
        """
    )
    parser.add_argument("input", help="Input Markdown file or directory")
    parser.add_argument("-o", "--output", help="Output DOCX file or directory")
    parser.add_argument("--no-toc", action="store_true", help="Don't generate table of contents")

    args = parser.parse_args()

    # Prepare extra arguments
    extra_args = ['--standalone', '--syntax-highlighting=pygments', '--preserve-tabs', '--wrap=preserve']

    if os.path.isdir(args.input):
        batch_convert(args.input, args.output, extra_args)
    else:
        md_to_docx(args.input, args.output, extra_args)
