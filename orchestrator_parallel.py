"""
Orquestador paralelo optimizado para metodología Viara:
- Estrategia y Contexto se ejecutan de forma secuencial optimizada
- Crítico recibe contexto completo para validación específica
- Pipeline robusto con manejo de errores
"""

from concurrent.futures import ThreadPoolExecutor
from agents.estrategia import agente_estrategia
from agents.contexto import agente_contexto
from agents.critico import agente_critico
from utils.loader import load_json

def run_pipeline_parallel(consulta_usuario: str, cliente_file: str) -> str:
    """
    Ejecuta pipeline completo de metodología Viara.
    
    Args:
        consulta_usuario: Solicitud específica del usuario
        cliente_file: Nombre del archivo JSON del cliente
        
    Returns:
        Contenido final optimizado y validado
    """
    # Cargar contexto completo del cliente
    contexto_cliente = load_json(f"data/clientes/{cliente_file}")

    with ThreadPoolExecutor(max_workers=2) as pool:
        # 1. Ejecutar Agente Estrategia (metodología Viara)
        fut_estrategia = pool.submit(agente_estrategia, consulta_usuario, contexto_cliente)

        # 2. Cuando termine Estrategia, ejecutar Agente Contexto (adaptación de marca)
        def _run_contexto():
            contenido_estrategia = fut_estrategia.result()
            return agente_contexto(contenido_estrategia, contexto_cliente)
        
        fut_contexto = pool.submit(_run_contexto)

        # 3. Obtener resultado de contexto
        contenido_adaptado = fut_contexto.result()

    # 4. Ejecutar Agente Crítico con contexto completo para validación específica
    contenido_final = agente_critico(contenido_adaptado, contexto_cliente)
    
    return contenido_final

# Script de prueba optimizado
if __name__ == "__main__":
    print("🤖 Ejecutando VIARA - Metodología completa")
    print("=" * 50)
    
    try:
        resultado = run_pipeline_parallel(
            "Genera una malla de contenido para diciembre enfocada en aumentar ventas",
            "everest_cocktails.json"
        )
        print("✅ Pipeline ejecutado exitosamente")
        print("\n📋 RESULTADO:")
        print("-" * 30)
        print(resultado)
        
    except Exception as e:
        print(f"❌ Error en pipeline: {str(e)}")
