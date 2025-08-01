# 🤖 Chatbot Multiagente VIARA
### *Asistente de Marketing Digital con IA Local*

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Descripción

**VIARA** es un chatbot multiagente modular diseñado específicamente para agencias de marketing digital. Utiliza **OpenAI GPT-4o mini** para generar contenido de alta calidad de forma rápida y eficiente.

### 🎯 **¿Para qué sirve?**

- **Generación de mallas de contenido** personalizadas por cliente
- **Estrategias de marketing digital** adaptadas a cada marca
- **Copys y contenido** optimizado para redes sociales
- **Flujo de trabajo profesional** con revisión y pulido automático

## 🏗️ Arquitectura del Sistema

```
[Consulta Usuario] 
    ↓
[Orquestador Paralelo]
    ├── 🧠 Agente Estrategia (Genera ideas y planificación)
    ├── 🎨 Agente Contexto (Adapta al cliente específico)  
    └── ✨ Agente Crítico (Revisa y pule el resultado)
    ↓
[Respuesta Final Optimizada]
```

### **Flujo Multiagente:**
1. **Estrategia**: Procesa la consulta usando las metodologías de tu agencia
2. **Contexto**: Adapta el contenido al tono y características del cliente específico
3. **Crítico**: Revisa, mejora y garantiza calidad humana (no AI-detectable)

## 🚀 Instalación Rápida

### **Prerrequisitos**
- Python 3.10+
- [API Key de OpenAI](https://platform.openai.com/api-keys)

### **1. Clonar el repositorio**
```bash
git clone https://github.com/Hacanaval/chatbot_multiagentico_viara.git
cd chatbot_multiagentico_viara
```

### **2. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **3. Configurar OpenAI**
```bash
# Crear archivo de configuración
echo "OPENAI_API_KEY=tu_api_key_aqui" > .env
echo "OPENAI_MODEL=gpt-4o-mini" >> .env
echo "OPENAI_TEMPERATURE_DEFAULT=0.3" >> .env

# Verificar que funciona
python test_openai.py
```

### **4. Probar el sistema**
```bash
python orchestrator_parallel.py
```

## 📁 Estructura del Proyecto

```
chatbot_multiagentico_viara/
│
├── 🎯 orchestrator_parallel.py    # Orquestador principal (recomendado)
├── 🔄 orchestrator_autogen.py     # Alternativa con AutoGen
│
├── agents/                        # 🤖 Lógica de cada agente
│   ├── estrategia.py              # Genera estrategias de contenido
│   ├── contexto.py                # Adapta al cliente específico
│   └── critico.py                 # Revisa y pule resultados
│
├── prompts/                       # 📝 Prompts modulares editables
│   ├── estrategia.md              # Template del agente estratégico
│   ├── contexto.md                # Template del adaptador de contexto
│   └── critico.md                 # Template del revisor crítico
│
├── data/                          # 📊 Datos de configuración
│   ├── instrucciones.json         # Metodología de tu agencia
│   └── clientes/                  # Configuraciones por cliente
│       └── everest_cocktails.json # Ejemplo: cliente de cocteles
│
├── utils/                         # 🛠️ Funciones auxiliares
│   ├── llm_client.py              # Cliente para OpenAI GPT-4o mini
│   ├── loader.py                  # Carga archivos JSON/MD
│   └── llm_config_autogen.py      # Config para AutoGen
│
├── memory/                        # 💾 Memoria conversacional (v2.0)
│   └── chat_logs/                 # Historial futuro
│
└── requirements.txt               # Dependencias del proyecto
```

## 🎮 Uso Básico

### **Ejecución Directa**
```python
from orchestrator_parallel import run_pipeline_parallel

resultado = run_pipeline_parallel(
    consulta_usuario="Genera una malla de contenido para septiembre",
    cliente_file="everest_cocktails.json"
)
print(resultado)
```

### **Personalizar Cliente**
1. Copia `data/clientes/everest_cocktails.json`
2. Edita los datos de tu cliente:
```json
{
  "empresa": "Tu Cliente",
  "sector": "Industria específica",
  "menciones_estrategicas": {
    "tono": "profesional y cercano",
    "hashtags_frecuentes": ["#TuMarca", "#Industria"]
  }
}
```

### **Ajustar Metodología**
Edita `data/instrucciones.json` con tus procesos internos:
```json
{
  "tono": "Tu tono característico",
  "frecuencia_publicacion": "Frecuencia deseada",
  "metodologia": ["Paso 1", "Paso 2", "..."]
}
```

## 🎨 Personalización de Prompts

Los prompts están externalizados en `prompts/*.md` para fácil edición:

- **`estrategia.md`**: Define cómo generar estrategias
- **`contexto.md`**: Controla la adaptación por cliente  
- **`critico.md`**: Establece criterios de calidad

**Ejemplo de personalización:**
```markdown
# prompts/estrategia.md
Eres el **Planner Estratégico** de [TU AGENCIA].

### Instrucciones específicas:
- Siempre incluir 3 pilares de contenido
- Mínimo 10 ideas por malla
- Formato: Carrusel > Reel > Historia
```

## ⚙️ Configuración Avanzada

### **Cambiar Modelo LLM**
```python
# En utils/llm_client.py
def run_llm(prompt: str, model: str = "gpt-4o-mini"):  # Cambiar aquí
```

### **Ajustar Temperatura**
```python
# En agents/critico.py
return run_llm(prompt, temperature=0.1)  # Más conservador
```

### **Orquestador AutoGen** (Alternativo)
```python
from orchestrator_autogen import run_pipeline_autogen

resultado = run_pipeline_autogen(
    consulta_usuario="Tu consulta",
    cliente_file="cliente.json"
)
```

## 🧪 Testing

```bash
# Test básico del orquestador
python orchestrator_parallel.py

# Test con cliente específico
python -c "from orchestrator_parallel import run_pipeline_parallel; print(run_pipeline_parallel('Test', 'everest_cocktails.json'))"
```

## 🛣️ Roadmap

### **v1.0 (Actual) ✅**
- [x] Arquitectura multiagente funcional
- [x] Prompts modulares editables
- [x] Configuración por cliente
- [x] Orquestación paralela optimizada

### **v2.0 (Próximo) 🚧**
- [ ] Memoria conversacional persistente
- [ ] Interfaz web con Streamlit
- [ ] Métricas de calidad automáticas
- [ ] Templates de mallas predefinidos

### **v3.0 (Futuro) 🔮**
- [ ] Integración con APIs de RRSS
- [ ] Análisis de competencia automático
- [ ] Generación de imágenes con AI
- [ ] Dashboard de rendimiento
