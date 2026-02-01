import streamlit as st
import streamlit.components.v1 as components
import time

# 1. Configuración de la página
st.set_page_config(
    page_title="¡Feliz Cumpleaños Sra. Flor!",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS AVANZADO (Diseño y Responsividad)
st.markdown("""
    <style>
    /* Importar fuente tipo 'tiza' de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

    /* Fondo general de la aplicación (Pizarra verde con viñeta para dar profundidad) */
    .stApp {
        background-color: #2b4e3e;
        background-image: radial-gradient(circle, #3a6351 0%, #1e3b2e 100%);
    }

    /* Estilos de texto globales */
    h1, h2, p, div, span, button {
        font-family: 'Patrick Hand', cursive !important;
        color: #f0f0f0 !important;
    }

    /* Título Principal */
    .title-text {
        text-align: center;
        font-size: 50px !important;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Subtítulo (Nombre) */
    .name-text {
        text-align: center;
        font-size: 60px !important;
        color: #ffcc00 !important; /* Amarillo */
        margin-top: -20px;
        text-shadow: 2px 2px 0px #4a4a4a;
        border-bottom: 2px dashed #f0f0f0;
        padding-bottom: 20px;
    }

    /* Cuerpo del mensaje */
    .message-text {
        text-align: center;
        font-size: 28px !important;
        margin-top: 20px;
        line-height: 1.5;
    }

    /* Emojis grandes */
    .big-emojis {
        font-size: 50px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* ESTILO DEL BOTÓN (Borrador de pizarra) */
    .stButton > button {
        width: 100%;
        background-color: #8B4513 !important; /* Color madera/borrador */
        color: white !important;
        border: 2px solid #deb887;
        font-size: 24px !important;
        padding: 10px 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        background-color: #A0522D !important;
        border-color: #fff;
    }

    /* MENSAJE DE FELICITACIÓN FINAL (Reemplazo de st.success) */
    .final-message {
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1); /* Transparente */
        border: 2px solid #ffcc00;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        font-size: 35px !important;
        color: #ffcc00 !important;
        animation: popIn 0.5s ease-out;
    }

    @keyframes popIn {
        0% { transform: scale(0); opacity: 0; }
        80% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); }
    }
    
    /* Ocultar elementos molestos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
    """, unsafe_allow_html=True)

# 3. JAVASCRIPT DE LLUVIA (Optimizado)
school_rain_js = """
<script>
    function throwSchoolItems() {
        const doc = window.parent.document;
        const emojis = ['✏️', '📚', '🍎', '📏', '📎', '🎓', '💯', '🌟'];
        
        const container = doc.createElement('div');
        container.style.position = 'fixed';
        container.style.top = '0';
        container.style.left = '0';
        container.style.width = '100vw';
        container.style.height = '100vh';
        container.style.pointerEvents = 'none';
        container.style.zIndex = '99999';
        doc.body.appendChild(container);

        const styleSheet = doc.createElement("style");
        styleSheet.innerText = `
            @keyframes fallRotate {
                0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
                100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
            }
            .school-item { position: absolute; top: -10vh; }
        `;
        doc.head.appendChild(styleSheet);

        for (let i = 0; i < 60; i++) {
            const item = doc.createElement('div');
            item.classList.add('school-item');
            item.innerText = emojis[Math.floor(Math.random() * emojis.length)];
            const size = Math.random() * 40 + 20; 
            item.style.fontSize = size + 'px';
            item.style.left = Math.random() * 95 + 'vw'; // Evitar scroll horizontal
            const duration = Math.random() * 3 + 3;
            item.style.animation = `fallRotate ${duration}s linear forwards`;
            item.style.animationDelay = Math.random() * 2 + 's';
            container.appendChild(item);
        }
        
        setTimeout(() => { container.remove(); styleSheet.remove(); }, 6000);
    }
    throwSchoolItems();
</script>
"""

# --- ESTRUCTURA VISUAL (Layout) ---

# Espacio superior
st.write("")

# Títulos con clases personalizadas
st.markdown('<p class="title-text">✨ ¡Feliz Cumpleaños! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="name-text">Sra. Flor</p>', unsafe_allow_html=True)

# Mensaje
st.markdown("""
    <div class="message-text">
        <p>Que tenga un lindo día.</p>
        <p>¡La quiero mucho!</p>
    </div>
    <div class="big-emojis">
        🎓 💐 📝
    </div>
""", unsafe_allow_html=True)

# --- BOTÓN CENTRADO ---
# Usamos columnas vacías a los lados para centrar.
# En móvil (pantalla pequeña), las columnas se adaptan.
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    presionado = st.button("🎁 Presione aquí 🎁")

# --- LÓGICA AL PRESIONAR ---
if presionado:
    # 1. Globos nativos
    st.balloons()
    
    # 2. Lluvia escolar (JavaScript)
    components.html(school_rain_js, height=0, width=0)
    
    # 3. Mensaje Final CENTRADO y ESTILIZADO (Sin usar st.success)
    st.markdown("""
        <div class="final-message">
            ¡Muchas Felicidades! <br>❤️
        </div>
    """, unsafe_allow_html=True)