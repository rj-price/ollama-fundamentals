import ollama

def main():
    model = "llama3.2:1b"

    while True:
        prompt = input("Please enter a prompt (or 'quit' to exit): ")

        if prompt.lower() == "quit":
            break

        try:
            response = ollama.chat(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                    ],
                stream=True
                )

            for chunk in response:
                print(chunk["message"]["content"], end="", flush=True)
            print("\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
