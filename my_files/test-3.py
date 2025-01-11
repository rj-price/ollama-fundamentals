import ollama

# Create a new model with modelfile
modelfile = """
FROM llama3.2
SYSTEM You are an experience molecular biologists who knows everything about fungal biology. You are very succinct and informative.
PARAMETER temperature 0.1
"""

ollama.create(model="molbiol", modelfile=modelfile)

res = ollama.generate(model="molbiol", prompt="tell me about fungal cell walls ")

print(res["response"])

# Delete model
#ollama.delete("molbiol")