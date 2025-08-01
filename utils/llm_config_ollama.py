from autogen.oai.client import OpenAIWrapper

# Ollama corre en http://localhost:11434
OLLAMA_BASE = "http://localhost:11434/v1"

def ollama_cfg(model="phi3:mini", temp=0.4):
    return {
        "cache_seed": 42,
        "base_url": OLLAMA_BASE,
        "api_type": "openai",
        "api_key": "ollama-key",     # literalmente así; Ollama no valida la key
        "model": model,
        "temperature": temp,
        # Wrapper evita que AutoGen use funciones no soportadas por Ollama
        "client": OpenAIWrapper,
    }

