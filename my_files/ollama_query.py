import ollama

# Initialise the Ollama client
client = ollama.Client()

# Define model and prompt
model = "llama3.2:1b"
prompt = "Tell me a joke"

# Send query to the model
reponse = client.generate(model=model, prompt=prompt)

# Print response
print(reponse.response)