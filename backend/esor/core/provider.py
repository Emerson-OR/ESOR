import ollama


class OllamaProvider:
    def __init__(self, model: str):
        self.model = model

    def generate(self, messages: list[dict[str, str]]) -> str:
        response = ollama.chat(
            model=self.model,
            messages=messages,
        )

        return response.message.content