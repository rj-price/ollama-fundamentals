import ollama
import os

model = "llama3.2:1b"

# Paths to input and output files
input_file = "./data/grocery_list.txt"
output_file = "./data/sorted_grocery_list.txt"

# Check if input exists
if not os.path.exists(input_file):
    print(f"Input file '{input_file}' not found.")
    exit(1)
    
# Read grocery items from imput
with open(input_file, "r") as f:
    items = f.read().strip()
    
# Prepare prompt for the model
prompt = f"""
You are an assistant that categorises and sorts grocery items. 
I am in the UK, so please use UK naming conventions (ie. in the UK 'Chips' are fries not potato chips).

Here is a list of grocery items:
{items}

Please:
- Categorise these items into appropriate categories, such as Produce, Dairy, Meat, Bakery, Beverages, etc.
- Sort the items alphabetically within each category.
- Present the categorised list in a clear and organized manner, using bullet points.
- List the total number of items at the bottom.
"""

# Send the prompt and get the response
try:
    response = ollama.generate(model=model, prompt=prompt)
    generated_text = response.get("response", "")
    
    # Write sorted list to output
    with open(output_file, "w") as f:
        f.write(generated_text.strip())
        
    print(f"Categorised list has been saved to '{output_file}'.")
except Exception as e:
    print("An error occurred:", str(e))