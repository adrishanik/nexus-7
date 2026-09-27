import requests
import json

class LocalLLMEngine:
    """Interface for offline local inference running on Orange Pi 5 NPU/CPU."""
    def __init__(self, model="tinyllama:1.1b", api_url="http://127.0.0.1:11434/api/generate"):
        self.model = model
        self.api_url = api_url

    def generate_response(self, prompt, max_tokens=100):
        payload = {
            "model": self.model,
            "prompt": f"System: You are Nexus-7, an autonomous assistant robot. Keep answers concise.\nUser: {prompt}\nAssistant:",
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": 0.6
            }
        }
        try:
            res = requests.post(self.api_url, json=payload, timeout=15)
            if res.status_code == 200:
                return res.json().get("response", "Operational.")
            return "Local inference communication error."
        except Exception as e:
            return f"LLM offline: {str(e)}"
          
