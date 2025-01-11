import ollama
import os

model = "llama3.2"

# Paths to input and output files
input_file = "./data/album_list.txt"
output_file = "./data/sorted_album_list.txt"

# Check if input exists
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)
    
# Read grocery items from imput
with open(input_file, "r") as f:
    items = f.read().strip()
    
# Prepare prompt for the model
prompt = f"""
You are a music expert that categorises and sorts a list of albums. 

Here is a list of artists and albums:
{items}

Please:
- Categorise these artists into appropriate genres.
- Sort the artists alphabetically within each genre.
- Present the categorised list in a clear and organized manner, using bullet points.
"""

# Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    print("==== Sorted Albums: ===== \n")
    print(generated_text)
    
    # Write sorted list to output
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
        
    print(f"Categorised list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))