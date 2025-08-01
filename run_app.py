#!/usr/bin/env python3
"""
Script de inicio para la aplicación VIARA
Ejecuta: python run_app.py
"""

import subprocess
import sys
from pathlib import Path

def main():
    """Ejecuta la aplicación Streamlit de VIARA."""
    
    # Verificar que estamos en el directorio correcto
    if not Path("main.py").exists():
        print("❌ Error: main.py no encontrado")
        print("   Asegúrate de ejecutar este script desde la raíz del proyecto")
        sys.exit(1)
    
    # Verificar que las dependencias están instaladas
    try:
        import streamlit
        import ollama
        print("✅ Dependencias verificadas")
    except ImportError as e:
        print(f"❌ Error: Dependencia faltante: {e}")
        print("   Ejecuta: pip install -r requirements.txt")
        sys.exit(1)
    
    print("🚀 Iniciando VIARA - Chatbot Multiagente")
    print("   Abriéndose en el navegador...")
    print("   Para detener: Ctrl+C")
    print("")
    
    # Ejecutar Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "main.py",
            "--server.address", "localhost",
            "--server.port", "8501",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 VIARA detenido. ¡Hasta la próxima!")
    except Exception as e:
        print(f"❌ Error al iniciar la aplicación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()