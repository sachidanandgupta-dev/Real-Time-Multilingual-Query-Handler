from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    try:
        lang = detect(text)
        print(f"[LANG] Detected language: {lang}")
        return lang
    except Exception as e:
        print(f"[LANG] Detection error: {e}")
        return "en"

def translate_text(text, target="en"):
    try:
        print(f"[TRANSLATE] Translating to {target}: {text[:50]}...")
        result = GoogleTranslator(source="auto", target=target).translate(text)
        print(f"[TRANSLATE] Result: {result[:50]}...")
        return result
    except Exception as e:
        print(f"[TRANSLATE] Error: {e}")
        return text