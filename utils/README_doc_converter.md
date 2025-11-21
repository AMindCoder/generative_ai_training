# Markdown to DOCX Converter

Convert Markdown files to DOCX format for easy import into Google Docs.

## Installation

1. Install Python dependencies:
```bash
pip install pypandoc
```

2. Install Pandoc (required):
- **macOS**: `brew install pandoc`
- **Linux**: `sudo apt-get install pandoc`
- **Windows**: Download from [pandoc.org](https://pandoc.org/installing.html)

## Usage

### Convert a single file
```bash
python md_to_doc_converter.py your_file.md
```

### Convert with custom output path
```bash
python md_to_doc_converter.py your_file.md -o output.docx
```

### Convert all Markdown files in a directory
```bash
python md_to_doc_converter.py ./markdown_directory/ -o ./docx_output/
```

### Convert without table of contents
```bash
python md_to_doc_converter.py your_file.md --no-toc
```

## Importing to Google Docs

After conversion, upload the DOCX file to Google Docs:
1. Go to [docs.google.com](https://docs.google.com)
2. Click **File** → **Open** → **Upload**
3. Select your converted DOCX file
4. The file will be imported and ready to edit

## Python API

You can also use the converter in your Python scripts:

```python
from md_to_doc_converter import md_to_docx, batch_convert

# Convert a single file
md_to_docx('input.md', 'output.docx')

# Batch convert
docx_files = batch_convert('./markdown_files/', './docx_files/')
```

## Features

- Preserves Markdown formatting (headings, lists, code blocks, etc.)
- Automatically generates table of contents
- Syntax highlighting for code blocks
- Batch conversion support
- Compatible with Google Docs import
