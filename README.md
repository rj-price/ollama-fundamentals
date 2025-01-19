<!-- @format -->
# Ollama Course – Build AI Apps Locally

[YouTube Video](https://www.youtube.com/watch?v=GWB9ApTPTv4&t=5054s)

Learn how to set up and use Ollama to build powerful AI applications locally. This hands-on course covers pulling and customizing models, REST APIs, Python integrations, and real-world projects like a Grocery List Organizer, RAG System, and an AI Recruiter Agency. Perfect for developers and AI enthusiasts ready to bring their ideas to life with local LLMs. Don’t miss the exclusive BONUS project at the end!

### Ollama Basics
See `commands_and_scripts.md` for basics of how to use Ollama and REST API.

### Ollama via Python
Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

Install requests
```bash
pip install requests
```

Generate jokes via REST API
```bash
python my_files/test-1.py
```

Generate simple code via Ollama library
```bash
pip install ollama

python my_files/test-2.py
```

Create new model and interact via Ollama library
```bash
python my_files/test-3.py
```

### Grocery Categoriser
Use Python with Ollama library to import and catergorise a grocery list.
```bash
python my_files/grocery_categoriser.py
```

Rewrite to create an album categoriser.
```bash
python my_files/music_categoriser.py
```

### Retrieval-Augmented Generation (RAG)
Activate virutal environment and install required libraries.
```bash
source venv/bin/activate
pip install -r requirements.txt
```

Using LangChain with our LRG1 preprint.
```bash
python my_files/rag/pdf-rag.py
```

Run interactive GUI using Streamlit.
```bash
streamlit run my_files/rag/pdf-rag-streamlit.py
```

---

## ADDITIONAL
Alternative simple method to query model using Ollama library.
```bash
python ollama_query.py
```

Iterate through models with the same prompt to compare outputs.
```bash
python model_comp.py
```

Interactive prompt input.
```bash
python prompt_input.py
```
