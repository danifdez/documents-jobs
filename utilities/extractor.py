import sys
import argparse
import os
from processors.html_processor import process_html
from processors.doc_processor import process_doc
from processors.pdf_processor import process_pdf
from processors.txt_processor import process_txt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process document files and extract text.")
    parser.add_argument("file_path", help="Path to the file to process")
    args = parser.parse_args()

    try:
        _, ext = os.path.splitext(args.file_path)
        ext = ext.lower()

        if ext in ['.html', '.htm']:
            with open(args.file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            print(process_html(html_content), flush=True)
        elif ext in ['.doc', '.docx']:
            print(process_doc(args.file_path), flush=True)
        elif ext in ['.pdf']:
            print(process_pdf(args.file_path), flush=True)
        elif ext in ['.txt']:
            print(process_txt(args.file_path), flush=True)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)
