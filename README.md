
# Markdown to PDF Converter

This Python script converts Markdown files to PDF using `markdown2` and `pdfkit` libraries.

## Requirements

- Python 3.x
- markdown2
- pdfkit
- wkhtmltopdf

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/downloads/).
2. Install required Python packages using pip:

   ```bash
   pip install markdown2 pdfkit
   ```

3. Install `wkhtmltopdf` from [wkhtmltopdf website](https://wkhtmltopdf.org/downloads.html).

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/tushar-asodariya/markdown-to-pdf-generator.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd markdown-to-pdf-generator
   ```

3. Run the script:

   ```bash
   python resume_generator.py
   ```

## How it works

1. The script reads Markdown content from a specified file.
2. It converts Markdown to HTML using `markdown2` library.
3. CSS style is applied to change the font to Arial, sans-serif.
4. PDF is generated from HTML using `pdfkit`.
5. The output PDF is saved with the specified filename.

## Example

Suppose you have a Markdown file named `resume.md` and you want to convert it to PDF with custom font:

```python
input_md_file = './resume.md'
output_pdf_file = 'Resume.pdf'

md_to_pdf(input_md_file, output_pdf_file)
```


