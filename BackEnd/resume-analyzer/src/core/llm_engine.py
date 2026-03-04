import requests
import json
from .config import OLLAMA_URL, OLLAMA_MODEL, REQUEST_TIMEOUT


def call_llm(prompt: str) -> dict:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise Exception("AI service unavailable")

    raw_output = response.json().get("response", "").strip()

    # Sometimes models wrap JSON in ```json blocks
    if raw_output.startswith("```"):
        raw_output = raw_output.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw_output)
    except json.JSONDecodeError:
        raise Exception("Invalid AI JSON response")