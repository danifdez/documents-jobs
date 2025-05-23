import json
import re
from trafilatura import extract
from bs4 import BeautifulSoup


def process_html(html_content):
    extracted = extract(
        html_content, output_format="html", favor_precision=True, include_formatting=True, include_links=True, include_images=True, include_tables=True)

    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title.string if soup.title else "No Title"
    metadata = {}
    for meta_tag in soup.find_all("meta"):
        name = meta_tag.get("name") or meta_tag.get("property")
        content = meta_tag.get("content")
        if name and content:
            metadata[name] = content

    if extracted:
        try:
            clean_soup = BeautifulSoup(extracted, "html.parser")

            is_fragment = not clean_soup.find('html')

            for tag in clean_soup.find_all(True):
                if tag.has_attr('style'):
                    del tag['style']
                if tag.has_attr('class'):
                    del tag['class']
                if tag.has_attr('id'):
                    del tag['id']

            for div in clean_soup.find_all('div'):
                if not div.find(['div', 'p', 'ul', 'ol', 'table', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    div.name = 'p'

            if is_fragment:
                top_elements = [
                    el for el in clean_soup.children if el.name is not None]

                if len(top_elements) == 1 and top_elements[0].name == 'div':
                    top_elements[0].unwrap()

            else:
                body = clean_soup.find('body')
                if body:
                    body_elements = [
                        el for el in body.children if el.name is not None]

                    if len(body_elements) == 1 and body_elements[0].name == 'div':
                        body_elements[0].unwrap()

            divs_to_check = list(clean_soup.find_all('div'))
            for div in divs_to_check:
                if not div.attrs and len([c for c in div.children if c.name == 'div']) == 1 and len([c for c in div.children if c.name is not None]) == 1:
                    div.unwrap()

            for div in clean_soup.find_all('div'):
                div.unwrap()

            if not is_fragment:
                body = clean_soup.find('body')
                if body:
                    body_html = ''.join(str(content)
                                        for content in body.contents)
                    clean_soup = BeautifulSoup(body_html, 'html.parser')
                else:
                    html_tag = clean_soup.find('html')
                    if html_tag:
                        head = clean_soup.find('head')
                        if head:
                            head.decompose()

            for tag in clean_soup.find_all(['head', 'script', 'style']):
                tag.decompose()

            clean_html = str(clean_soup).strip()

            clean_html = re.sub(r'\s+', ' ', clean_html)
            clean_html = re.sub(r'<p>\s*</p>', '', clean_html)
            clean_html = re.sub(
                r'<html>|</html>|<body>|</body>', '', clean_html)

            extracted = clean_html.strip()
        except Exception as e:
            print(f"Error processing HTML content: {str(e)}")

    if extracted:
        extracted = extracted.strip()

    return json.dumps({"content": extracted, "title": title, "metadata": metadata})
