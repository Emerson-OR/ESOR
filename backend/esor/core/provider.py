import ollama

from esor.core.config import MODEL_NAME, SYSTEM_PROMPT


class OllamaProvider:
    def __init__(self, model: str = MODEL_NAME):
        self.model = model

    def generate(self, message: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response.message.content