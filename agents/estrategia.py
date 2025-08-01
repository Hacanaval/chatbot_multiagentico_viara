"""Agente Estrategia: Especialista en pasos 2, 3, 4 de metodología Viara.

ESPECIALIZACIÓN ÚNICA:
1. Definición de objetivos y pilares de contenido (Paso 2)
2. Creación de banco de ideas específicas (Paso 3)
3. Construcción de malla de contenido semanal (Paso 4)

LÍMITES ESTRICTOS:
- NO genera copys finales
- NO adapta tono de marca  
- NO valida contenido
- SOLO estructura estratégica

Entrada: Consulta usuario + Contexto cliente + Metodología Viara
Salida: Estrategia digital estructurada (pilares + ideas + malla)
"""

from utils.loader import load_json, load_prompt
from utils.llm_client import run_llm
import json

def agente_estrategia(consulta_usuario: str, contexto_cliente: dict) -> str:
    """
    Genera SOLO la estructura estratégica siguiendo pasos 2, 3, 4 de metodología Viara.
    
    Args:
        consulta_usuario: Solicitud específica del usuario
        contexto_cliente: JSON completo con datos del cliente
        
    Returns:
        Estructura estratégica: pilares + banco de ideas + malla semanal
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
    
    # Ejecutar con temperatura baja para mayor consistencia en estructura
    return run_llm(prompt, temperature=0.3)
