from esor.core.config import MODEL_NAME
from esor.core.conversation import ConversationManager
from esor.core.provider import OllamaProvider


def main():
    conversation = ConversationManager()
    ai = OllamaProvider(model=MODEL_NAME)

    print("=" * 40)
    print("              ESOR")
    print("       Local AI Assistant")
    print("=" * 40)
    print("Escribe 'salir' para terminar.\n")

    while True:
        message = input("Tú: ").strip()

        if not message:
            continue

        if message.lower() in {"salir", "exit", "quit"}:
            print("\nESOR: Hasta luego, Emerson.")
            break

        conversation.add_user_message(message)

        response = ai.generate(
            conversation.get_messages()
        )

        conversation.add_assistant_message(response)

        print(f"\nESOR: {response}\n")


if __name__ == "__main__":
    main()