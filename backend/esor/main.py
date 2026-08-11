from esor.core.provider import OllamaProvider


def main():
    ai = OllamaProvider()

    print("=" * 40)
    print("              ESOR")
    print("       Local AI Assistant")
    print("=" * 40)

    message = input("\nTú: ")

    response = ai.generate(message)

    print(f"\nESOR: {response}")


if __name__ == "__main__":
    main()