from agents.estrategia import agente_estrategia
from agents.contexto  import agente_contexto
from agents.critico   import agente_critico
from utils.loader     import load_json

# 1) ------------- Ajusta estos dos parámetros -------------
cliente_file = "everest_cocktails.json"
consulta     = "Genera una malla de contenido para septiembre"
# -----------------------------------------------------------

cliente = load_json(f"data/clientes/{cliente_file}")

# --- Estrategia ---
salida_estrategia = agente_estrategia(consulta, cliente)
print("\n========== SALIDA ESTRATEGIA ==========\n")
print(salida_estrategia)
print("\nPalabras:", len(salida_estrategia.split()), "\n")

# --- Contexto ---
salida_contexto = agente_contexto(salida_estrategia, cliente)
print("\n========== SALIDA CONTEXTO ==========\n")
print(salida_contexto)
print("\nPalabras:", len(salida_contexto.split()), "\n")

# --- Crítico ---
salida_critico = agente_critico(salida_contexto)
print("\n========== SALIDA CRÍTICO ==========\n")
print(salida_critico)
print("\nPalabras:", len(salida_critico.split()), "\n")

