import markdown2
import pdfkit

def md_to_pdf(md_file, pdf_file):
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

# Configure pdfkit to use the correct wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    # Read the Markdown content from the file
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content)

    # Specify CSS style to change font
    css = 'body { font-family: Arial, sans-serif; }'

    # Generate PDF from HTML with custom options including CSS
    pdfkit.from_string(html_content, pdf_file, css='./style.css',configuration=config)

if __name__ == "__main__":
    # Specify the input Markdown file and the output PDF file
    input_md_file = './resume.md'
    output_pdf_file = 'Tushar Asodariya-Flutter_developer_4_yrs_experience.pdf'

    # Convert Markdown to PDF with custom font
    md_to_pdf(input_md_file, output_pdf_file)
