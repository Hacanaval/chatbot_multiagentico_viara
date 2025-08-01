"""Agente Estrategia: genera la propuesta inicial de contenido.

Tomamos:
1. Instrucciones de la agencia (JSON)
2. Consulta del usuario
3. Plantilla de prompt

Devolvemos la respuesta del LLM.
"""

from utils.loader import load_json, load_prompt
from utils.ollama_client import run_llm
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

def agente_estrategia(consulta_usuario: str, contexto_cliente: dict) -> str:
    instrucciones = load_json("data/instrucciones.json")
    tpl = load_prompt("prompts/estrategia.md")
    prompt = tpl.format(
        instrucciones_agencia=json.dumps(instrucciones, indent=2, ensure_ascii=False),
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False),
        consulta_usuario=consulta_usuario
    )
    return run_llm(prompt)


