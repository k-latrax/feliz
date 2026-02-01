import streamlit as st
import streamlit.components.v1 as components
import random  # Importante para que la animación salga siempre

# 1. Configuración de la página
st.set_page_config(
    page_title="¡Feliz Cumpleaños Sra. Flor!",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS MAESTRO (Centrado forzoso y Diseño)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

    /* Fondo */
    .stApp {
        background-color: #2b4e3e;
        background-image: radial-gradient(circle, #3a6351 0%, #1e3b2e 100%);
    }

    /* Tipografía */
    * {
        font-family: 'Patrick Hand', cursive !important;
        color: #f0f0f0;
    }

    /* Títulos */
    .title-text {
        text-align: center;
        font-size: 45px !important;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 0;
    }
    
    .name-text {
        text-align: center;
        font-size: 60px !important;
        color: #ffcc00 !important;
        text-shadow: 2px 2px 0px #4a4a4a;
        border-bottom: 2px dashed #f0f0f0;
        padding-bottom: 20px;
        margin-bottom: 30px;
    }

    /* Texto del mensaje */
    .message-text {
        text-align: center;
        font-size: 26px !important;
    }

    /* Emojis */
    .big-emojis {
        font-size: 45px;
        text-align: center;
        margin: 20px 0;
    }

    /* --- CORRECCIÓN DEFINITIVA DEL BOTÓN --- */
    
    /* Esto centra el contenedor del botón */
    .stButton {
        display: flex;
        justify-content: center;
        width: 100%;
    }

    /* Esto da estilo al botón y asegura que no se estire feo en móvil */
    .stButton > button {
        background-color: #8B4513 !important;
        color: white !important;
        border: 2px solid #deb887 !important;
        font-size: 24px !important;
        padding: 12px 40px !important;
        border-radius: 15px !important;
        box-shadow: 0px 5px 0px #5e2f0d !important; /* Efecto 3D */
        transition: all 0.1s;
        margin: 0 auto !important; /* Centrado extra de seguridad */
        display: block !important;
    }

    .stButton > button:active {
        box-shadow: 0px 2px 0px #5e2f0d !important;
        transform: translateY(3px);
    }

    /* Mensaje Final */
    .final-message {
        text-align: center;
        border: 2px solid #ffcc00;
        border-radius: 15px;
        padding: 20px;
        margin-top: 30px;
        font-size: 30px !important;
        color: #ffcc00 !important;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    @keyframes popIn {
        0% { transform: scale(0); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu, header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. FUNCIÓN GENERADORA DE LLUVIA (Con truco anti-cache)
def generar_lluvia():
    # Generamos un ID único cada vez para engañar al navegador
    unique_id = random.randint(0, 1000000)
    
    js_code = f"""
    <div id="rain-container-{unique_id}"></div>
    <script>
        (function() {{
            const doc = window.parent.document;
            const emojis = ['✏️', '📚', '🍎', '📏', '📎', '🎓', '💯', '🌟', '💖'];
            
            // Si ya existe un contenedor viejo, bórralo (limpieza)
            const oldContainer = doc.getElementById('school-rain-container');
            if (oldContainer) oldContainer.remove();

            const container = doc.createElement('div');
            container.id = 'school-rain-container';
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
                @keyframes fallRotate {{
                    0% {{ transform: translateY(-10vh) rotate(0deg); opacity: 1; }}
                    100% {{ transform: translateY(110vh) rotate(720deg); opacity: 0; }}
                }}
                .school-item {{ position: absolute; top: -10vh; }}
            `;
            doc.head.appendChild(styleSheet);

            for (let i = 0; i < 60; i++) {{
                const item = doc.createElement('div');
                item.classList.add('school-item');
                item.innerText = emojis[Math.floor(Math.random() * emojis.length)];
                const size = Math.random() * 40 + 20; 
                item.style.fontSize = size + 'px';
                item.style.left = Math.random() * 90 + 'vw'; 
                const duration = Math.random() * 3 + 3;
                item.style.animation = `fallRotate ${{duration}}s linear forwards`;
                item.style.animationDelay = Math.random() * 2 + 's';
                container.appendChild(item);
            }}
            
            // Limpieza automática
            setTimeout(() => {{ 
                container.remove(); 
                styleSheet.remove(); 
            }}, 6000);
        }})();
    </script>
    """
    return js_code

# --- ESTRUCTURA VISUAL ---

st.write("") 

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

# --- BOTÓN ---
# Nota: Ya no usamos columnas, el CSS se encarga de centrarlo
presionado = st.button("🎁 Presione aquí 🎁")

if presionado:
    st.balloons()
    # Llamamos a la función con el truco del ID aleatorio
    components.html(generar_lluvia(), height=0, width=0)
    
    st.markdown("""
        <div class="final-message">
            ¡Muchas Felicidades! <br>❤️
        </div>
    """, unsafe_allow_html=True)