import ollama

# Initialise the Ollama client
client = ollama.Client()

# Extract list of available models
ollama_models = ollama.list().models
models = [model.model for model in ollama_models]

# Define prompt
prompt = "Tell me a joke"

# Send query to the models
for model in models:
    reponse = client.generate(model=model, prompt=prompt)
    print(f"### Response from {model} ###")
    print(reponse.response, "\n")