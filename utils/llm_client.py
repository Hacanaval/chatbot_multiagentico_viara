import os
from dotenv import load_dotenv

# Cargar variables de entorno (forzar recarga)
load_dotenv(override=True)

def run_llm(prompt: str,
            model: str = "gpt-4o-mini",
            temperature: float | None = None) -> str:
    """
    Cliente LLM para VIARA - Usando OpenAI GPT-4o mini exclusivamente.
    
    Args:
        prompt: Texto a enviar al modelo
        model: Modelo de OpenAI (por defecto: gpt-4o-mini)
        temperature: Temperatura de generación (por defecto: 0.3)
    
    Returns:
        Respuesta del modelo como string
    """
    # Configuración por defecto - SOLO OPENAI
    if model is None:
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    
    if temperature is None:
        temperature = float(os.getenv("OPENAI_TEMPERATURE_DEFAULT", "0.3"))
    
    # Ejecutar con OpenAI API directamente
    try:
        from openai import OpenAI
        
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key or api_key == "your_openai_api_key_here":
            raise ValueError("🚨 ERROR: OPENAI_API_KEY no configurada en .env")
        
        # Limpiar la API key de saltos de línea y espacios
        api_key = api_key.replace('\n', '').replace(' ', '').strip()
        
        client = OpenAI(api_key=api_key)
        
        max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", "2000"))
        
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
        
    except ImportError:
        raise ImportError("🚨 ERROR: 'pip install openai' requerido")
    except Exception as e:
        raise Exception(f"🚨 ERROR OpenAI: {str(e)}")
