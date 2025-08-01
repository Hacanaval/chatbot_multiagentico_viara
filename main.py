"""
Frontend Streamlit para Chatbot Multiagente VIARA
Interfaz completa para generar contenido de marketing digital
"""

import streamlit as st
import json
import os
from pathlib import Path
from typing import Dict, List, Any
import traceback

# Imports del proyecto
from utils.loader import load_json, save_json, load_prompt, save_prompt
from orchestrator_parallel import run_pipeline_parallel

# Configuración de la página
st.set_page_config(
    page_title="VIARA - Chatbot Multiagente",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Funciones auxiliares
@st.cache_data
def get_available_clients() -> List[str]:
    """Obtiene la lista de archivos JSON de clientes disponibles."""
    clients_dir = Path("data/clientes")
    if not clients_dir.exists():
        return []
    return [f.name for f in clients_dir.glob("*.json")]

@st.cache_data
def get_available_prompts() -> Dict[str, str]:
    """Obtiene la lista de prompts disponibles."""
    prompts_dir = Path("prompts")
    prompts = {}
    if prompts_dir.exists():
        for f in prompts_dir.glob("*.md"):
            prompts[f.stem] = f.name
    return prompts

def validate_json(text: str) -> tuple[bool, Dict[str, Any] | None, str]:
    """Valida si un texto es JSON válido."""
    try:
        parsed = json.loads(text)
        return True, parsed, ""
    except json.JSONDecodeError as e:
        return False, None, f"Error JSON: {str(e)}"

def show_success_message(message: str):
    """Muestra mensaje de éxito."""
    st.success(f"✅ {message}")

def show_error_message(message: str):
    """Muestra mensaje de error."""
    st.error(f"❌ {message}")

# Título principal
st.title("🤖 VIARA - Chatbot Multiagente")
st.subheader("Asistente de Marketing Digital con IA Local")
st.divider()

# Layout de tres columnas
col_left, col_center, col_right = st.columns([1, 2, 1])

# ================== COLUMNA IZQUIERDA: MENÚ LATERAL ==================
with col_left:
    st.header("📋 Configuración")
    
    # 1. SELECCIÓN DE CLIENTE
    st.subheader("👤 Cliente")
    available_clients = get_available_clients()
    
    if not available_clients:
        st.warning("No se encontraron clientes en data/clientes/")
        selected_client = None
    else:
        selected_client = st.selectbox(
            "Seleccionar cliente:",
            available_clients,
            index=0,
            help="Elige el cliente para personalizar el contenido"
        )
    
    st.divider()
    
    # 2. EDITOR DE PROMPTS
    st.subheader("📝 Editar Prompts")
    available_prompts = get_available_prompts()
    
    for agent_name, prompt_file in available_prompts.items():
        with st.expander(f"Prompt {agent_name.capitalize()}"):
            try:
                current_prompt = load_prompt(f"prompts/{prompt_file}")
                
                edited_prompt = st.text_area(
                    f"Contenido del prompt {agent_name}:",
                    value=current_prompt,
                    height=200,
                    key=f"prompt_{agent_name}"
                )
                
                if st.button(f"💾 Guardar {agent_name}", key=f"save_prompt_{agent_name}"):
                    try:
                        save_prompt(f"prompts/{prompt_file}", edited_prompt)
                        show_success_message(f"Prompt {agent_name} guardado correctamente")
                        st.cache_data.clear()  # Limpiar cache
                        st.rerun()
                    except Exception as e:
                        show_error_message(f"Error al guardar prompt {agent_name}: {str(e)}")
                        
            except Exception as e:
                st.error(f"Error al cargar prompt {agent_name}: {str(e)}")

# ================== COLUMNA CENTRAL: GENERACIÓN DE CONTENIDO ==================
with col_center:
    st.header("🎯 Generación de Contenido")
    
    # Área de consulta
    user_query = st.text_area(
        "💬 Escribe tu consulta:",
        placeholder="Ej: Genera una malla de contenido para septiembre enfocada en aumentar el engagement...",
        height=120,
        help="Describe qué tipo de contenido o estrategia necesitas"
    )
    
    # Botón de generación
    generate_col1, generate_col2, generate_col3 = st.columns([1, 2, 1])
    with generate_col2:
        generate_button = st.button(
            "🚀 Generar Contenido",
            type="primary",
            use_container_width=True,
            disabled=not selected_client or not user_query.strip()
        )
    
    st.divider()
    
    # Área de resultado
    if generate_button and selected_client and user_query.strip():
        with st.spinner("🤖 Generando contenido con IA multiagente..."):
            try:
                # Ejecutar pipeline
                result = run_pipeline_parallel(user_query.strip(), selected_client)
                
                # Mostrar resultado
                st.subheader("✨ Resultado Final")
                st.markdown("---")
                
                # Resultado en contenedor expandible
                with st.container():
                    st.markdown(result)
                
                # Opción de descarga
                st.download_button(
                    label="📥 Descargar Resultado",
                    data=result,
                    file_name=f"contenido_viara_{selected_client.replace('.json', '')}.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                show_error_message(f"Error al generar contenido: {str(e)}")
                with st.expander("🔍 Ver detalles del error"):
                    st.code(traceback.format_exc())
    
    elif generate_button:
        if not selected_client:
            show_error_message("Por favor, selecciona un cliente")
        if not user_query.strip():
            show_error_message("Por favor, escribe una consulta")

# ================== COLUMNA DERECHA: EDITOR DE CLIENTE ==================
with col_right:
    st.header("⚙️ Datos del Cliente")
    
    if selected_client:
        try:
            # Cargar datos del cliente
            client_data = load_json(f"data/clientes/{selected_client}")
            
            # Mostrar nombre del cliente
            client_name = client_data.get("empresa", "Cliente")
            st.subheader(f"📊 {client_name}")
            
            # Editor JSON
            st.write("**Editar configuración:**")
            
            # Convertir a JSON bonito para edición
            json_str = json.dumps(client_data, indent=2, ensure_ascii=False)
            
            edited_json_str = st.text_area(
                "Datos del cliente (JSON):",
                value=json_str,
                height=400,
                help="Edita los datos del cliente en formato JSON"
            )
            
            # Validación en tiempo real
            is_valid, parsed_data, error_msg = validate_json(edited_json_str)
            
            if not is_valid:
                st.error(f"JSON inválido: {error_msg}")
            else:
                st.success("✅ JSON válido")
            
            # Botón guardar cliente
            if st.button("💾 Guardar Cliente", disabled=not is_valid):
                try:
                    save_json(f"data/clientes/{selected_client}", parsed_data)
                    show_success_message(f"Cliente {client_name} guardado correctamente")
                    st.cache_data.clear()  # Limpiar cache
                    st.rerun()
                except Exception as e:
                    show_error_message(f"Error al guardar cliente: {str(e)}")
            
            st.divider()
            
            # Información rápida del cliente
            st.write("**Resumen rápido:**")
            if "sector" in client_data:
                st.write(f"**Sector:** {client_data['sector']}")
            if "menciones_estrategicas" in client_data and "tono" in client_data["menciones_estrategicas"]:
                st.write(f"**Tono:** {client_data['menciones_estrategicas']['tono']}")
            if "canales_activos" in client_data:
                canales = list(client_data["canales_activos"].keys())
                st.write(f"**Canales:** {', '.join(canales)}")
                
        except Exception as e:
            show_error_message(f"Error al cargar cliente {selected_client}: {str(e)}")
    else:
        st.info("👆 Selecciona un cliente para ver y editar sus datos")

# ================== PIE DE PÁGINA ==================
st.divider()
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.write("**🤖 VIARA v1.0**")
    st.caption("Chatbot Multiagente Local")

with col_footer2:
    st.write("**🔒 Privacidad**")
    st.caption("100% Local con Ollama")

with col_footer3:
    st.write("**📊 Estado**")
    if selected_client:
        st.caption(f"Cliente: {selected_client}")
    else:
        st.caption("Sin cliente seleccionado")

# ================== INICIALIZACIÓN ==================
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.cache_data.clear()