#!/usr/bin/env python3
"""
Demo rápido de VIARA - Chatbot Multiagente
Muestra el flujo completo sin interfaz gráfica
"""

import json
from orchestrator_parallel import run_pipeline_parallel
from utils.loader import load_json

def main():
    """Ejecuta una demostración completa del sistema."""
    
    print("🤖 DEMO: VIARA - Chatbot Multiagente")
    print("=" * 60)
    print()
    
    # Casos de prueba
    test_cases = [
        {
            "cliente": "everest_cocktails.json",
            "consulta": "Genera una malla de contenido para diciembre enfocada en fiestas navideñas"
        },
        {
            "cliente": "restaurante_gourmet.json", 
            "consulta": "Crea contenido para promocionar nuestro menú de San Valentín"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"📋 CASO {i}: {test['cliente'].replace('.json', '').replace('_', ' ').title()}")
        print("-" * 40)
        
        # Cargar info del cliente
        try:
            client_data = load_json(f"data/clientes/{test['cliente']}")
            print(f"💼 Cliente: {client_data['empresa']}")
            print(f"🎯 Sector: {client_data['sector']}")
            print(f"📝 Consulta: {test['consulta']}")
            print()
            
            print("⚡ Ejecutando pipeline multiagente...")
            print("  1️⃣ Agente Estrategia: Generando ideas...")
            print("  2️⃣ Agente Contexto: Adaptando al cliente...")
            print("  3️⃣ Agente Crítico: Puliendo resultado...")
            print()
            
            # Ejecutar pipeline (comentado para no hacer llamadas reales a LLM en demo)
            # resultado = run_pipeline_parallel(test['consulta'], test['cliente'])
            
            # Resultado simulado para demo
            resultado_simulado = f"""
ESTRATEGIA DE CONTENIDO - {client_data['empresa']}

🎯 OBJETIVO GLOBAL
Aumentar engagement y conversiones durante {test['consulta'].split()[-1] if 'diciembre' in test['consulta'] else 'la campaña especial'}

📊 PILARES ESTRATÉGICOS
• Conexión emocional con la audiencia
• Showcase de productos premium
• Experiencias únicas de marca
• Contenido generado por usuarios

💡 BANCO DE IDEAS
1. Behind the scenes - Atraer - Reel - "Descubre cómo..."
2. Testimoniales - Convertir - Historia - "Compra ahora"
3. Trends & challenges - Fidelizar - Carrusel - "Participa"
4. Producto estrella - Convertir - Reel - "Oferta limitada"
5. Tips & consejos - Atraer - Carrusel - "Aprende más"

📅 MALLA RECOMENDADA (SEMANAL)
• Lunes: Inspiración (Pilar 1)
• Miércoles: Producto (Pilar 2) 
• Viernes: Comunidad (Pilar 3)
• Domingo: Behind scenes (Pilar 4)

#{client_data['menciones_estrategicas']['hashtags_frecuentes'][0]} #MarketingDigital #ContenidoDeCalidad
            """.strip()
            
            print("✨ RESULTADO GENERADO:")
            print("=" * 50)
            print(resultado_simulado)
            print("=" * 50)
            print()
            
        except Exception as e:
            print(f"❌ Error en caso {i}: {str(e)}")
            print()
        
        if i < len(test_cases):
            print("⏳ Continuando con siguiente caso...")
            print("\n" + "🔄 " * 20 + "\n")
    
    print("🎉 DEMO COMPLETADO")
    print()
    print("🚀 Para usar VIARA completo:")
    print("   python run_app.py")
    print()
    print("📖 Para más información:")
    print("   cat README.md")
    print("   cat INSTALL.md")

if __name__ == "__main__":
    main()