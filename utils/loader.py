"""Funciones de carga de JSON y plantillas de prompt.

Centralizamos rutas para que todo el proyecto lea archivos del mismo modo.
"""

import json
import pathlib

# Carpeta raíz del proyecto
BASE = pathlib.Path(__file__).resolve().parent.parent

def load_json(relative_path: str):
    """Leemos un archivo JSON y devolvemos el objeto Python."""
    full_path = BASE / relative_path
    with full_path.open(encoding="utf-8") as f:
        return json.load(f)

def load_prompt(relative_path: str):
    """Leemos un prompt *.md y devolvemos su texto."""
    full_path = BASE / relative_path
    return full_path.read_text(encoding="utf-8")

def save_json(relative_path: str, data: dict):
    """Guardamos un dict como JSON bonito."""
    full_path = BASE / relative_path
    full_path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

def save_prompt(relative_path: str, text: str):
    """Guardamos texto en un prompt *.md*."""
    full_path = BASE / relative_path
    full_path.write_text(text, encoding="utf-8")
