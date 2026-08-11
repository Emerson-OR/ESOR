import ollama

from esor.core.config import MODEL_NAME, SYSTEM_PROMPT


class OllamaProvider:
    def __init__(self, model: str = MODEL_NAME):
        self.model = model
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            }
        ]

    def generate(self, message: str) -> str:
        self.messages.append(
            {
                "role": "user",
                "content": message,
            }
        )

        response = ollama.chat(
            model=self.model,
            messages=self.messages,
        )

        assistant_message = response.message.content

        self.messages.append(
            {
                "role": "assistant",
                "content": assistant_message,
            }
        )

        return assistant_message