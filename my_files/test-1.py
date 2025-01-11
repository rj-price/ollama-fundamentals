import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "tell me 5 science based jokes"
}

response = requests.post(url, json=data, stream=True)

# check response status
if response.status_code == 200:
    print("Generated Text:\n", end=" ", flush=True)
    # Iterate over the streaming response
    for line in response.iter_lines():
        if line:
            # Decode the line and parse the JSON
            decoded_line = line.decode("utf-8")
            result = json.loads(decoded_line)
            # Get the text from the response
            generated_text = result.get("response", "")
            print(generated_text, end="", flush=True)
    print("")
else:
    print("Error:", response.status_code, response.text)
