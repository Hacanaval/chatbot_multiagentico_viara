"""Agente Crítico: Especialista en validación final y garantía de calidad.

ESPECIALIZACIÓN ÚNICA:
1. Validación de coherencia de marca
2. Garantía de calidad humana (anti-IA)
3. Alineación estratégica con objetivos del cliente

LÍMITES ESTRICTOS:
- NO genera nueva estrategia
- NO adapta tono de marca
- NO cambia estructura del contenido
- SOLO valida y optimiza calidad final

Entrada: Contenido personalizado + Contexto completo del cliente
Salida: Contenido validado y optimizado para máxima calidad profesional
"""

from utils.loader import load_prompt
from utils.ollama_client import run_llm
import json

def agente_critico(contenido_prev: str, contexto_cliente: dict, 
                   temperature: float = 0.1) -> str:
    """
    Valida SOLO la calidad final del contenido según estándares Viara.
    
    Args:
        contenido_prev: Contenido personalizado por agente contexto
        contexto_cliente: JSON completo con datos del cliente para validación específica
        temperature: Temperatura muy baja para máxima consistencia en validación
        
    Returns:
        Contenido final validado (igual o con optimizaciones mínimas de calidad)
    """
    template = load_prompt("prompts/critico.md")
    
    # Construir prompt con contenido y contexto completo para validación técnica
    prompt = template.format(
        contenido_prev=contenido_prev,
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False)
    )
    
    # Ejecutar con temperatura muy baja para máxima consistencia en validación
    return run_llm(prompt, temperature=temperature)
