"""
Orquestador AutoGen (AG2) para Viara.
– Estratega y Adaptador corren en paralelo.
– Crítico pule al final.
"""

# -------------------- IMPORTS --------------------
from autogen.agentchat import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
from autogen.agentchat.tools import PythonTool

from utils.llm_config_ollama import ollama_cfg
from agents.estrategia import agente_estrategia
from agents.contexto  import agente_contexto
from agents.critico   import agente_critico
from utils.loader import load_json

# -------------------- TOOLS ----------------------
tool_estrategia = PythonTool.from_function(
        agente_estrategia,
        name="estrategia_tool",
        description="Genera la estrategia base con metodología Viara")

tool_contexto   = PythonTool.from_function(
        agente_contexto,
        name="contexto_tool",
        description="Adapta la estrategia al tono y datos del cliente")

tool_critico    = PythonTool.from_function(
        agente_critico,
        name="critico_tool",
        description="Pulido final (humano, sin emojis)")

# -------------------- AGENTES --------------------
estratega = AssistantAgent(
        name="Estratega",
        llm_config=ollama_cfg(temp=0.4),
        tools=[tool_estrategia])

adaptador = AssistantAgent(
        name="Adaptador",
        llm_config=ollama_cfg(temp=0.4),
        tools=[tool_contexto])

critico = AssistantAgent(
        name="Crítico",
        llm_config=ollama_cfg(temp=0.2),
        tools=[tool_critico])

usuario = UserProxyAgent(          # no pedirá input humano
        name="Usuario",
        human_input_mode="NEVER",
        llm_config=False)

# -------------------- RUN PIPELINE ---------------
def run_pipeline_autogen(consulta: str, cliente_file: str) -> str:
    """Ejecuta Estratega + Adaptador en paralelo y luego Crítico."""
    cliente = load_json(f"data/clientes/{cliente_file}")

    # Mensaje inicial que contiene todo el contexto
    system_prompt = (
        "Consulta del usuario:\n"
        f"{consulta}\n\n"
        "Datos del cliente (JSON):\n"
        f"{cliente}\n\n"
        "Instrucciones:\n"
        "- Estratega llama a estrategia_tool y no responde nada más.\n"
        "- Adaptador espera la salida de Estratega y llama a contexto_tool.\n"
        "- Crítico espera y llama a critico_tool con el texto ya adaptado.\n"
        'Devuelve únicamente la versión final pulida y luego escribe "TERMINATE".'
    )

    # Cargamos el mensaje en el groupchat
    gc = GroupChat(
        agents=[usuario, estratega, adaptador, critico],
        messages=[{"role": "user", "content": system_prompt}],
        max_round=8,
        speaker_selection_method="round_robin",
    )
    manager = GroupChatManager(
        groupchat=gc, 
        llm_config=ollama_cfg(temp=0))

    # Disparamos el chat
    usuario.initiate_chat(
        manager,
        message="Iniciar",
        summary_method="last_msg",
    )

    return manager.chat_history[-1]["content"]
