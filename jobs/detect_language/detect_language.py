import sys
from langdetect import detect


def detect_language(text):
    """Detect language of given text and return the language code."""
    try:
        return detect(text)
    except Exception as e:
        return f"Error detecting language: {e}"

