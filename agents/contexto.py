"""Agente Contexto: Especialista en adaptación de marca.

ESPECIALIZACIÓN ÚNICA:
1. Adaptar contenido estratégico al ADN de la marca
2. Personalizar tono y vocabulario específico del cliente  
3. Integrar hashtags y referencias naturalmente

LÍMITES ESTRICTOS:
- NO genera nueva estrategia
- NO valida contenido
- NO cambia estructura
- SOLO personaliza tono al ADN de marca

Entrada: Contenido estratégico + Contexto completo del cliente
Salida: Contenido personalizado 100% al tono y estilo de la marca
"""

from utils.loader import load_prompt
from utils.llm_client import run_llm
import json

def agente_contexto(contenido_prev: str, contexto_cliente: dict) -> str:
    """
    Adapta SOLO el tono del contenido estratégico al ADN específico de la marca.
    
    Args:
        contenido_prev: Contenido estratégico generado por agente estrategia
        contexto_cliente: JSON completo con datos del cliente
        
    Returns:
        Contenido con MISMO contenido pero personalizado al tono de la marca
    """
    template = load_prompt("prompts/contexto.md")
    
    # Extraer tono específico con fallback seguro
    tono = contexto_cliente.get("menciones_estrategicas", {}).get("tono", "profesional y cercano")
    
    # Construir prompt con todos los parámetros necesarios
    prompt = template.format(
        contenido_prev=contenido_prev,
        contexto_cliente=json.dumps(contexto_cliente, indent=2, ensure_ascii=False),
        tono=tono
    )
    
    # Ejecutar con temperatura moderada para personalización creativa pero controlada
    return run_llm(prompt, temperature=0.4)
