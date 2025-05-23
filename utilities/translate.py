from transformers import pipeline
import sys
import json


def translate(source, target, texts):
    """Detect language of given text and return the language code."""
    try:
        translation = pipeline(
            "translation", model=f"Helsinki-NLP/opus-mt-{source}-{target}")
        output = translation(texts)
        translated_texts = [item['translation_text'] for item in output]
        return json.dumps(translated_texts)
    except Exception as e:
        return f"Error detecting language: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = []
        source = sys.argv[1]
        target = sys.argv[2]
        for arg in sys.argv[3:]:
            if (arg.startswith('"') and arg.endswith('"')) or (arg.startswith("'") and arg.endswith("'")):
                arg = arg[1:-1]
                args.append(arg)
        print(translate(source, target, args))
