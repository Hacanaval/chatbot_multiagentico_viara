"""Agente Crítico: Validador senior especializado en marketing digital.

Especializado en:
1. Validación de coherencia de marca
2. Garantía de calidad humana (anti-IA)
3. Alineación estratégica con objetivos del cliente

Entrada: Contenido final + Contexto completo del cliente
Salida: Contenido validado y optimizado para máxima calidad
"""

from utils.loader import load_prompt
from utils.ollama_client import run_llm
import json

def agente_critico(contenido_prev: str, contexto_cliente: dict, 
                   temperature: float = 0.1) -> str:
    """
    Valida y optimiza contenido final según estándares Viara.
    
    Args:
        contenido_prev: Contenido adaptado por agente contexto
        contexto_cliente: JSON completo con datos del cliente para validación
        temperature: Temperatura del modelo (muy baja para consistencia)
        
    Returns:
        Contenido final validado y optimizado
    """
    template = load_prompt("prompts/critico.md")
    
    # Construir prompt con contenido y contexto completo para validación
    prompt = template.format(
        contenido_prev=contenido_prev,
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False)
    )
    
    # Ejecutar con temperatura muy baja para máxima consistencia
    return run_llm(prompt, temperature=temperature)
