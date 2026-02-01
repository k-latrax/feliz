import streamlit as st
import streamlit.components.v1 as components

# 1. Configuración de la página
st.set_page_config(
    page_title="¡Feliz Cumpleaños Sra. Flor!",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS AVANZADO (Diseño, Fuentes y Centrado Absoluto)
st.markdown("""
    <style>
    /* Importar fuente tipo 'tiza' de Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

    /* Fondo general */
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
        font-size: 45px !important;
        margin-bottom: 0px;
        text-shadow: 2px 2px 4px #000000;
        line-height: 1.2;
    }

    /* Subtítulo (Nombre) */
    .name-text {
        text-align: center;
        font-size: 60px !important;
        color: #ffcc00 !important; /* Amarillo */
        margin-top: -10px;
        text-shadow: 2px 2px 0px #4a4a4a;
        border-bottom: 2px dashed #f0f0f0;
        padding-bottom: 20px;
        margin-bottom: 20px;
    }

    /* Cuerpo del mensaje */
    .message-text {
        text-align: center;
        font-size: 26px !important;
        line-height: 1.4;
    }

    /* Emojis grandes */
    .big-emojis {
        font-size: 45px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* --- CORRECCIÓN DEL BOTÓN (Centrado Absoluto) --- */
    
    /* 1. El contenedor del botón se vuelve flexible y centra su contenido */
    div.stButton {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    /* 2. El botón en sí mismo */
    div.stButton > button {
        background-color: #8B4513 !important; /* Color madera */
        color: white !important;
        border: 2px solid #deb887 !important;
        font-size: 22px !important;
        padding: 12px 30px !important; /* Relleno para que se vea bien */
        border-radius: 12px !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.3);
        transition: transform 0.2s;
        /* Quitamos el width: 100% para que no se estire feo, 
           ahora el tamaño depende del texto y se centra solo */
        width: auto !important; 
    }
    
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #A0522D !important;
        border-color: #fff !important;
    }

    /* MENSAJE DE FELICITACIÓN FINAL */
    .final-message {
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        border: 2px solid #ffcc00;
        border-radius: 15px;
        padding: 20px;
        margin-top: 30px; /* Separación del botón */
        font-size: 32px !important;
        color: #ffcc00 !important;
        animation: popIn 0.5s ease-out;
        width: 100%; /* Asegura que el mensaje ocupe el ancho disponible */
    }

    @keyframes popIn {
        0% { transform: scale(0); opacity: 0; }
        80% { transform: scale(1.1); opacity: 1; }
        100% { transform: scale(1); }
    }
    
    /* Ocultar elementos de la interfaz de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    </style>
    """, unsafe_allow_html=True)

# 3. JAVASCRIPT DE LLUVIA (Sin cambios, funciona bien)
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
            item.style.left = Math.random() * 95 + 'vw'; 
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

# --- ESTRUCTURA VISUAL ---

st.write("") # Espaciador superior

# Textos
st.markdown('<p class="title-text">✨ ¡Feliz Cumpleaños! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="name-text">Sra. Flor</p>', unsafe_allow_html=True)

st.markdown("""
    <div class="message-text">
        <p>Que tenga un lindo día.</p>
        <p>¡La quiero mucho!</p>
    </div>
    <div class="big-emojis">
        🎓 💐 📝
    </div>
""", unsafe_allow_html=True)

# --- BOTÓN (Sin columnas, centrado por CSS) ---
presionado = st.button("🎁 Presione aquí 🎁")

# --- LÓGICA AL PRESIONAR ---
if presionado:
    st.balloons()
    components.html(school_rain_js, height=0, width=0)
    
    st.markdown("""
        <div class="final-message">
            ¡Muchas Felicidades! <br>❤️
        </div>
    """, unsafe_allow_html=True)