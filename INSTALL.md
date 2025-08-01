# 🚀 Guía de Instalación - VIARA

## 📋 Requisitos Previos

### 1. Python 3.10+
```bash
python --version  # Debe ser 3.10 o superior
```

### 2. Instalar Ollama
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Descargar desde https://ollama.ai/download
```

### 3. Descargar modelo LLM
```bash
ollama pull phi3:mini
# o alternativamente:
ollama pull llama3:8b
```

## 📦 Instalación del Proyecto

### 1. Clonar repositorio
```bash
git clone https://github.com/Hacanaval/chatbot_multiagentico_viara.git
cd chatbot_multiagentico_viara
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv

# Activar entorno:
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🧪 Verificación de Instalación

### Test rápido del sistema
```bash
# Verificar backend
python orchestrator_parallel.py

# Verificar frontend
python run_app.py
```

## 🚀 Ejecutar VIARA

### Opción 1: Script de inicio (Recomendado)
```bash
python run_app.py
```

### Opción 2: Streamlit directo
```bash
streamlit run main.py
```

### Opción 3: Solo backend (sin UI)
```bash
python orchestrator_parallel.py
```

## 🛠️ Configuración Personalizada

### Cambiar modelo LLM
Edita `utils/ollama_client.py`:
```python
def run_llm(prompt: str, model: str = "llama3:8b"):  # Cambiar aquí
```

### Añadir nuevo cliente
1. Crea `data/clientes/mi_cliente.json`
2. Usa el formato de `everest_cocktails.json` como plantilla

### Personalizar prompts
Edita los archivos en `prompts/`:
- `estrategia.md` - Lógica de generación de estrategias
- `contexto.md` - Adaptación al cliente
- `critico.md` - Revisión y pulido final

## ❗ Solución de Problemas

### Ollama no responde
```bash
# Verificar que Ollama está corriendo
ollama list

# Reiniciar Ollama si es necesario
ollama serve
```

### Error de importación
```bash
# Reinstalar dependencias
pip install -r requirements.txt --upgrade
```

### Puerto ocupado
```bash
# Cambiar puerto en run_app.py o ejecutar:
streamlit run main.py --server.port 8502
```

## 🔧 Desarrollo

### Estructura de archivos importante
```
chatbot_multiagentico_viara/
├── main.py                    # 🖥️ Frontend Streamlit
├── orchestrator_parallel.py   # 🤖 Backend multiagente
├── run_app.py                 # 🚀 Script de inicio
├── agents/                    # 🧠 Lógica de agentes
├── prompts/                   # 📝 Templates editables
├── data/clientes/             # 👥 Configuraciones de cliente
└── utils/                     # 🛠️ Funciones auxiliares
```

### Comandos útiles
```bash
# Limpiar cache de Streamlit
streamlit cache clear

# Ver logs detallados
streamlit run main.py --logger.level debug

# Ejecutar en modo de desarrollo
streamlit run main.py --server.runOnSave true
```

¡Ya tienes VIARA listo para generar contenido de marketing digital! 🎉