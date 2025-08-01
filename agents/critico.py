"""Agente Crítico: revisa y pule el texto adaptado al cliente."""

from utils.loader import load_prompt
from utils.ollama_client import run_llm

def agente_critico(contenido_prev: str,
                   temperature: float | None = 0.2) -> str:
    """Pulimos el texto para entregar la versión final."""
    template = load_prompt("prompts/critico.md")
    prompt = template.format(contenido_prev=contenido_prev)
    return run_llm(prompt, temperature=temperature)
