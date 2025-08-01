"""Agente Estrategia: Implementa metodología Viara para estrategia digital.

Especializado en:
1. Definición de objetivos y pilares de contenido
2. Creación de banco de ideas específicas 
3. Construcción de malla de contenido semanal

Entrada: Consulta usuario + Contexto cliente + Metodología Viara
Salida: Estrategia digital estructurada y ejecutable
"""

from utils.loader import load_json, load_prompt
from utils.ollama_client import run_llm
import json

def agente_estrategia(consulta_usuario: str, contexto_cliente: dict) -> str:
    """
    Genera estrategia digital siguiendo metodología Viara.
    
    Args:
        consulta_usuario: Solicitud específica del usuario
        contexto_cliente: JSON completo con datos del cliente
        
    Returns:
        Estrategia digital estructurada con pilares, ideas y malla
    """
    # Cargar metodología Viara
    instrucciones = load_json("data/instrucciones.json")
    template = load_prompt("prompts/estrategia.md")
    
    # Construir prompt con todos los datos necesarios
    prompt = template.format(
        consulta_usuario=consulta_usuario,
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False),
        instrucciones_agencia=json.dumps(instrucciones, indent=2, ensure_ascii=False)
    )
    
    # Ejecutar con temperatura baja para mayor consistencia
    return run_llm(prompt, temperature=0.3)
