import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "gemini-flash-latest"

url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Say hello in one sentence."
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print(response.json())