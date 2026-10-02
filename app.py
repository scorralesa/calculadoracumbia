import streamlit as st
import math

# Configuración de la página
st.set_page_config(
    page_title="Predicción de Gusto Musical",
    page_icon="🎵",
    layout="centered"
)

# Estilo y Título
st.title("🎵 Calculadora de Afinidad Musical y Cortejo")
st.markdown("""
Esta aplicación utiliza un **modelo de regresión logística multivariante** derivado de un estudio empírico de audiencia ($N=53$). 
Responde las 4 preguntas para calcular matemáticamente tu probabilidad de disfrutar el **Reggaetón** frente a ritmos tradicionales como la **Cumbia** o el **Jarabe Tapatío**.
""")

st.divider()

# --- FORMULARIO DE INTERACCIÓN ---
st.subheader("📋 Responde las siguientes 4 preguntas:")

# Pregunta 1: Generación
gen_opcion = st.radio(
    "1. ¿A qué grupo generacional perteneces?",
    ["Generación Z (Menor de 27 años)", "Millennial (28 a 43 años)", "Generación X o Baby Boomer (44+ años)"],
    index=0
)

# Pregunta 2: Contacto físico / Baile
contacto_opcion = st.select_slider(
    "2. En una pista de baile, ¿qué tan cómodo/a te sientes con el contacto físico directo y la cadencia pélvica (estilo Lambada/Perreo)?",
    options=["Muy incómodo/a (Prefiero distancia)", "Neutral", "Muy cómodo/a"]
)

# Pregunta 3: Red Social
red_opcion = st.selectbox(
    "3. ¿Cuál es tu red social de consumo diario principal?",
    ["TikTok / Instagram", "Facebook", "Medios tradicionales / Ninguna de las anteriores"]
)

# Pregunta 4: Ambiente Festivo
ambiente_opcion = st.radio(
    "4. ¿Qué ambiente festivo prefieres?",
    ["Club / Evento Urbano Contemporáneo", "Fiesta Tradicional / Salón de Gala (Cumbia, Vals, Folclore)"],
    index=0
)

st.divider()

# --- BOTÓN DE CÁLCULO Y LÓGICA DEL MODELO ---
if st.button("🧮 Calcular mi Probabilidad", type="primary", use_container_width=True):
    # Intercepto base del modelo
    z = -0.20

    # 1. Mapeo Generacional
    if "Generación Z" in gen_opcion:
        z += 1.98
    elif "Millennial" in gen_opcion:
        z += 0.50
    else:
        z -= 2.30

    # 2. Mapeo Contacto
    if "Muy cómodo/a" in contacto_opcion:
        z += 1.35
    elif "Neutral" in contacto_opcion:
        z += 0.10
    else:
        z -= 1.25

    # 3. Mapeo Red Social
    if "TikTok / Instagram" in red_opcion:
        z += 0.85
    elif "Facebook" in red_opcion:
        z -= 0.35
    else:
        z -= 0.80

    # 4. Mapeo Ambiente
    if "Club" in ambiente_opcion:
        z += 1.20
    else:
        z -= 1.30

    # Función logística: P(Y=1) = 1 / (1 + e^-z)
    probabilidad = (1 / (1 + math.exp(-z))) * 100

    # --- RESULTADOS VISUALES ---
    st.subheader("📊 Resultado del Modelo Predictivo:")
    
    st.metric(label="Probabilidad Estimada de Gusto por el Reggaetón", value=f"{probabilidad:.1f}%")
    st.progress(int(probabilidad))

    if probabilidad >= 70:
        st.success("🔥 **AFINIDAD ALTA**: Tienes una probabilidad muy elevada de disfrutar el reggaetón y considerarlo una expresión válida de cortejo urbano contemporáneo.")
    elif 35 <= probabilidad < 70:
        st.warning("🎧 **AFINIDAD MODERADA / ECLÉCTICA**: Tu perfil muestra flexibilidad; disfrutas ritmos urbanos en contextos festivos, pero mantienes gusto por la cumbia y la salsa.")
    else:
        st.error("❄️ **AFINIDAD BAJA / TRADICIONAL**: Tu perfil demuestra una preferencia marcada por el cortejo de pareja suelta, la cumbia tradicional, el vals o el folclore señorial.")