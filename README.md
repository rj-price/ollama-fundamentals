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