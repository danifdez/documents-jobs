from docling.document_converter import DocumentConverter, InputFormat, PdfFormatOption, StandardPdfPipeline


def process_doc(file):
    pipeline_options = StandardPdfPipeline.get_default_options()
    pipeline_options.do_ocr = False

    pdf_format_option = PdfFormatOption(pipeline_options=pipeline_options)

    format_options = {InputFormat.PDF: pdf_format_option}
    converter = DocumentConverter(format_options=format_options)

    result = converter.convert(file)

    html_content = result.document.export_to_html()

    print(html_content)
