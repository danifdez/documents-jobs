import os
from jobs.extraction.processors.html_processor import process_html
from jobs.extraction.processors.doc_processor import process_doc
from jobs.extraction.processors.pdf_processor import process_pdf
from jobs.extraction.processors.txt_processor import process_txt


def extract(file_path: str) -> str:
    try:
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext in ['.html', '.htm']:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            return process_html(html_content)
        elif ext in ['.doc', '.docx']:
            return process_doc(file_path)
        elif ext in ['.pdf']:
            return process_pdf(file_path)
        elif ext in ['.txt']:
            return process_txt(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    except Exception as e:
        return None
