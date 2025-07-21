import langid
from functools import wraps
import time
import re
import requests

def detect_language(audio_content):
    # Placeholder: Use langid or Google STT hints
    # For demo, default to 'en-IN'
    return 'en-IN'

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if i == 2:
                    raise
                time.sleep(2 ** i)
    return wrapper

def estimate_confidence(response):
    # Placeholder: Use LLM metadata or heuristics
    return 0.8

def extract_topic(response):
    # Simple keyword-based topic extraction
    topics = ["landlord", "divorce", "cybercrime", "property", "marriage", "contract", "criminal", "civil"]
    for topic in topics:
        if topic in response.lower():
            return topic
    return "general"

def detect_human_request(text):
    keywords = ["human", "lawyer", "talk to a lawyer", "real person"]
    return any(kw in text.lower() for kw in keywords)

def translate_text(text, target_language):
    """
    Translate text to the target_language using Google Translate API (free endpoint).
    target_language: e.g., 'hi' for Hindi, 'en' for English
    """
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            'client': 'gtx',
            'sl': 'auto',
            'tl': target_language,
            'dt': 't',
            'q': text,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            result = response.json()
            return ''.join([item[0] for item in result[0]])
        else:
            return text  # fallback to original
    except Exception as e:
        print(f"Translation error: {e}")
        return text 