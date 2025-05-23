import sys
from langdetect import detect


def detect_language(text):
    """Detect language of given text and return the language code."""
    try:
        return detect(text)
    except Exception as e:
        return f"Error detecting language: {e}"


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(detect_language(text))
