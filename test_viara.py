#!/usr/bin/env python3
"""
Script de testing completo para VIARA optimizado
Verifica que todos los componentes funcionen correctamente
"""

import json
import traceback
from pathlib import Path

def test_estructura_archivos():
    """Verificar que todos los archivos necesarios existen"""
    print("🔍 Test 1: Estructura de archivos")
    
    archivos_requeridos = [
        "prompts/estrategia.md",
        "prompts/contexto.md", 
        "prompts/critico.md",
        "agents/estrategia.py",
        "agents/contexto.py",
        "agents/critico.py",
        "data/instrucciones.json",
        "data/clientes/everest_cocktails.json",
        "data/clientes/restaurante_gourmet.json",
        "orchestrator_parallel.py",
        "utils/loader.py",
        "utils/llm_client.py"
    ]
    
    for archivo in archivos_requeridos:
        if Path(archivo).exists():
            print(f"  ✅ {archivo}")
        else:
            print(f"  ❌ {archivo} - FALTA")
            return False
    
    print("  ✅ Todos los archivos necesarios existen\n")
    return True

def test_imports():
    """Verificar que todos los imports funcionan"""
    print("🔍 Test 2: Imports de módulos")
    
    try:
        from utils.loader import load_json, load_prompt, save_json, save_prompt
        print("  ✅ utils.loader")
        
        from utils.llm_client import run_llm
        print("  ✅ utils.llm_client")
        
        from agents.estrategia import agente_estrategia
        print("  ✅ agents.estrategia")
        
        from agents.contexto import agente_contexto
        print("  ✅ agents.contexto")
        
        from agents.critico import agente_critico
        print("  ✅ agents.critico")
        
        from orchestrator_parallel import run_pipeline_parallel
        print("  ✅ orchestrator_parallel")
        
    except Exception as e:
        print(f"  ❌ Error en imports: {str(e)}")
        return False
    
    print("  ✅ Todos los imports funcionan correctamente\n")
    return True

def main():
    """Ejecutar todos los tests"""
    print("🤖 VIARA - Test Suite Completo")
    print("=" * 50)
    print()
    
    tests = [
        test_estructura_archivos,
        test_imports
    ]
    
    resultados = []
    for test in tests:
        try:
            resultado = test()
            resultados.append(resultado)
        except Exception as e:
            print(f"❌ Error ejecutando test: {str(e)}")
            print(traceback.format_exc())
            resultados.append(False)
    
    print("📊 RESUMEN DE TESTS")
    print("=" * 30)
    if all(resultados):
        print("🎉 TODOS LOS TESTS PASARON")
        print("✅ VIARA está listo para funcionar")
        print()
        print("🚀 Siguiente paso: python orchestrator_parallel.py")
        print("🎯 O ejecutar: python run_app.py")
    else:
        print("❌ ALGUNOS TESTS FALLARON")
        print("🔧 Revisar los errores mostrados arriba")
    
    return all(resultados)

if __name__ == "__main__":
    main()
