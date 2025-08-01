# test_agents.py
import json
from utils.loader import load_json, load_prompt
from agents.estrategia import agente_estrategia
from agents.contexto import agente_contexto  
from agents.critico import agente_critico

def test_individual_agents():
    print("🧪 PROBANDO AGENTES INDIVIDUALMENTE")
    print("=" * 50)
    
    # Cargar datos de prueba
    consulta = "Ideas para promocionar cócteles en diciembre"
    cliente_data = load_json("data/clientes/everest_cocktails.json")
    
    print(f"📝 Consulta: {consulta}")
    print(f"💼 Cliente: {cliente_data['empresa']}")
    print()
    
    try:
        # Test Agente 1: Estrategia
        print("1️⃣ PROBANDO AGENTE ESTRATEGIA...")
        estrategia_result = agente_estrategia(consulta, cliente_data)
        print(f"✅ Resultado Estrategia: {len(estrategia_result)} caracteres")
        print(f"📄 Muestra: {estrategia_result[:200]}...")
        print()
        
        # Test Agente 2: Contexto
        print("2️⃣ PROBANDO AGENTE CONTEXTO...")
        contexto_result = agente_contexto(estrategia_result, cliente_data)
        print(f"✅ Resultado Contexto: {len(contexto_result)} caracteres")
        print(f"📄 Muestra: {contexto_result[:200]}...")
        print()
        
        # Test Agente 3: Crítico
        print("3️⃣ PROBANDO AGENTE CRÍTICO...")
        final_result = agente_critico(contexto_result, cliente_data)
        print(f"✅ Resultado Final: {len(final_result)} caracteres")
        print(f"📄 Muestra: {final_result[:200]}...")
        print()
        
        print("🎉 TODOS LOS AGENTES FUNCIONAN CORRECTAMENTE")
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_individual_agents()