import ollama

def run_llm(prompt: str,
            model: str = "phi3:mini",
            temperature: float | None = None) -> str:
    """Enviamos prompt al modelo local con opciones opcionales."""
    opts = {"temperature": temperature} if temperature is not None else {}

    respuesta = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options=opts            # << aquí viajan las opciones
    )
    return respuesta["message"]["content"]
