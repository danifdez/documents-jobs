from transformers import pipeline
import json


def translate(source, target, texts):
    """Detect language of given text and return the language code."""
    try:
        translation = pipeline(
            "translation", model=f"Helsinki-NLP/opus-mt-{source}-{target}")
        output = translation(texts)
        translated_texts = [item['translation_text'] for item in output]
        return translated_texts
    except Exception as e:
        return f"Error detecting language: {e}"
