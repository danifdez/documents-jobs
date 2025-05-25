from transformers import pipeline


def entities(text):
    pipe = pipeline("token-classification", model="dslim/bert-base-NER")
    result = pipe(text)
    parse_result = []

    for elements in result:
        for entity in elements:
            try:
                if '##' in entity['word']:
                    parse_result[-1]['word'] += entity['word'].replace(
                        '##', '')
                elif entity['entity'].startswith('B-'):
                    parse_result.append({
                        'word': entity['word'],
                        'entity': entity['entity'].split('-')[1],
                    })
                else:
                    parse_result[-1]['word'] += ' ' + entity['word']
            except:
                continue

    unique_result = []
    seen = set()
    for ent in parse_result:
        key = (ent['word'], ent['entity'])
        if key not in seen:
            seen.add(key)
            unique_result.append(ent)
    return unique_result
