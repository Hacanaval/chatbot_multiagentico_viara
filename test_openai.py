#!/usr/bin/env python3
"""
Test rápido de la nueva integración con OpenAI
"""

import os
from utils.llm_client import run_llm

def test_openai_integration():
    """Prueba la nueva integración con OpenAI GPT-4o mini."""
    
    print("🤖 TEST: OPENAI GPT-4O MINI INTEGRATION")
    print("=" * 50)
    
    # Verificar que existe el archivo .env
    if not os.path.exists('.env'):
        print("❌ ERROR: Archivo .env no encontrado")
        return False
    
    # Leer API key desde .env
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key or api_key == 'your_openai_api_key_here':
        print("🚨 NECESITAS CONFIGURAR TU API KEY DE OPENAI")
        print("📝 Edita el archivo .env y reemplaza:")
        print("   OPENAI_API_KEY=your_openai_api_key_here")
        print("   Con tu API key real de OpenAI")
        print()
        print("🔗 Obtén tu API key en: https://platform.openai.com/api-keys")
        return False
        
    print(f"✅ API Key configurada: {api_key[:8]}...{api_key[-4:]}")
    print()
    
    # Test básico
    try:
        print("🔥 PROBANDO OPENAI GPT-4O MINI...")
        
        import time
        start = time.time()
        
        response = run_llm(
            prompt="Responde solo: 'OpenAI GPT-4o mini funcionando perfectamente'"
        )
        
        duration = time.time() - start
        
        print(f"✅ Respuesta: {response}")
        print(f"⚡ Tiempo: {duration:.1f} segundos")
        print()
        
        if duration < 5:
            print("🚀 ¡EXCELENTE! OpenAI es súper rápido")
        else:
            print("⚠️ Respuesta lenta, pero funcional")
            
        return True
        
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

def test_viara_agent_with_openai():
    """Prueba rápida de un agente con OpenAI."""
    
    print("\n" + "=" * 50)
    print("🎯 TEST: AGENTE ESTRATEGIA CON OPENAI")
    print("=" * 50)
    
    try:
        from agents.estrategia import agente_estrategia
        from utils.loader import load_json
        
        # Datos de prueba simples
        consulta = "Ideas rápidas para promocionar cócteles"
        cliente_data = load_json("data/clientes/everest_cocktails.json")
        
        print(f"📝 Consulta: {consulta}")
        print(f"💼 Cliente: {cliente_data['empresa']}")
        print()
        
        print("🤖 Ejecutando agente estrategia con OpenAI...")
        
        import time
        start = time.time()
        
        # Aquí necesitaríamos modificar temporalmente el agente para usar OpenAI
        # Por ahora solo probamos que el sistema funciona
        
        result = agente_estrategia(consulta, cliente_data)
        
        duration = time.time() - start
        
        print(f"✅ Agente completado en {duration:.1f} segundos")
        print(f"📄 Resultado: {len(result)} caracteres")
        print(f"🔍 Muestra: {result[:150]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR en agente: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 INICIANDO TESTS DE OPENAI INTEGRATION")
    print()
    
    # Test 1: Conexión básica
    success1 = test_openai_integration()
    
    if success1:
        # Test 2: Agente con OpenAI (comentado hasta configurar API key)
        # success2 = test_viara_agent_with_openai()
        print("✅ Sistema listo para usar OpenAI")
        print()
        print("📋 PRÓXIMOS PASOS:")
        print("1. Configura tu API key en .env")
        print("2. Ejecuta: python test_openai.py")
        print("3. Si funciona, ejecuta: python quick_test.py")
    else:
        print("❌ Configura la API key primero")