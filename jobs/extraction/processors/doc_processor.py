from docling.document_converter import DocumentConverter, InputFormat, PdfFormatOption, StandardPdfPipeline
from bs4 import BeautifulSoup


def process_doc(file):
    pipeline_options = StandardPdfPipeline.get_default_options()
    pipeline_options.do_ocr = False

    pdf_format_option = PdfFormatOption(pipeline_options=pipeline_options)

    format_options = {InputFormat.PDF: pdf_format_option}
    converter = DocumentConverter(format_options=format_options)

    result = converter.convert(file)

    html_content = result.document.export_to_html()
    parsed_html = BeautifulSoup(html_content, "html.parser")

    for tag in parsed_html.find_all(True):
        if tag.has_attr('class'):
            del tag['class']
        if tag.has_attr('style'):
            del tag['style']

    for div in parsed_html.find_all('div'):
        if not div.find('div') and not div.find('p'):
            div.name = 'p'

    while parsed_html.find('div'):
        for div in parsed_html.find_all('div'):
            div.unwrap()

    body_content = ""
    if parsed_html.body:
        for child in parsed_html.body.children:
            if hasattr(child, 'name'):
                content = str(child).strip()
                if content:
                    body_content += content
            else:
                content = child.strip()
                if content:
                    body_content += f"<p>{content}</p>"

    body_content = body_content.strip()

    return {"content": body_content}
