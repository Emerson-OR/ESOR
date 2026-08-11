from esor.core.provider import OllamaProvider


def main():
    ai = OllamaProvider()

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

        response = ai.generate(message)

        print(f"\nESOR: {response}\n")


if __name__ == "__main__":
    main()