from utils.loader import load_json, load_prompt
from utils.ollama_client import run_llm
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent

def agente_contexto(contenido_prev: str, contexto_cliente: dict) -> str:
    tpl = load_prompt("prompts/contexto.md")
    prompt = tpl.format(
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False),
        tono=contexto_cliente.get("menciones_estrategicas", {}).get("tono", "neutro"),
        contenido_prev=contenido_prev
    )
    return run_llm(prompt)

