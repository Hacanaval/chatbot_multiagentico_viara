"""
Orquestador paralelo mínimo:
– Estrategia y Contexto se ejecutan simultáneamente en hilos.
– Crítico pule después.
"""

from concurrent.futures import ThreadPoolExecutor
from agents.estrategia import agente_estrategia
from agents.contexto  import agente_contexto
from agents.critico   import agente_critico
from utils.loader import load_json

def run_pipeline_parallel(consulta_usuario: str, cliente_file: str) -> str:
    contexto_cliente = load_json(f"data/clientes/{cliente_file}")

    with ThreadPoolExecutor(max_workers=2) as pool:
        # 1. Lanzo Estrategia
        fut_estrategia = pool.submit(agente_estrategia, consulta_usuario, contexto_cliente)

        # 2. Cuando Estrategia termine, Contexto usa su resultado
        def _run_contexto():
            contenido_prev = fut_estrategia.result()
            return agente_contexto(contenido_prev, contexto_cliente)
        fut_contexto = pool.submit(_run_contexto)

        # 3. Espero Contexto y aplico Crítico
        contenido_prev = fut_contexto.result()

    return agente_critico(contenido_prev)

# script de prueba rápida
if __name__ == "__main__":
    print(
        run_pipeline_parallel(
            "Genera una malla de contenido para septiembre",
            "everest_cocktails.json"
        )
    )
