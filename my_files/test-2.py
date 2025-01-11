import ollama

# == Chat example ==
response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "write a python function to find all of the prime numbers under 100"}
    ]
)

#print(response["message"]["content"])


# == Chat example streaming ==
response = ollama.chat(
    model="qwen2.5-coder:1.5b",
    messages=[
        {"role": "user", "content": "write a python function to find all of the prime numbers under 100"}
    ],
    stream=True
)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
    
print("")