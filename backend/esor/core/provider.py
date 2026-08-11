import ollama


class OllamaProvider:
    def __init__(self, model: str = "qwen3:4b"):
        self.model = model

    def generate(self, message: str) -> str:
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
        )

        return response.message.content