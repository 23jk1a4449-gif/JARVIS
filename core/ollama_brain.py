import requests


class OllamaBrain:
    def __init__(self, model="llama3.2:3b"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def ask(self, command):
        response = requests.post(
            self.url,
            json={
                "model": self.model,
                "prompt": (
                    "You are JARVIS, a helpful desktop AI assistant. "
                    "Answer clearly and briefly.\n\n"
                    f"User request: {command}"
                ),
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()
        return data["response"].strip()