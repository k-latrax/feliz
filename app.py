import streamlit as st
import streamlit.components.v1 as components
import random

# Configuración de la página
st.set_page_config(
    page_title="¡Feliz Cumpleaños Sra. Flor!",
    page_icon="🍎",
    layout="centered"
)

# --- CSS PARA EL TEMA PIZARRA Y BOTÓN ---
st.markdown("""
    <style>
    /* Fondo verde pizarra */
    .stApp {
        background-color: #2b4e3e;
        background-image: url("https://www.transparenttextures.com/patterns/blackboard.png");
    }
    
    /* Texto color tiza */
    h1, h2, h3, p, div, span, label {
        color: #f0f0f0 !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    
    /* Líneas de tiza */
    h1 {
        text-align: center;
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 10px;
    }
    
    /* Botón */
    .stButton>button {
        width: 100%;
        background-color: #ffcc00;
        color: #2b4e3e !important;
        border: 3px solid #ffffff;
        border-radius: 10px;
        font-weight: bold;
        font-size: 20px;
        padding: 10px 0;
        text-shadow: none;
    }
    .stButton>button:hover {
        background-color: #e6b800;
        border-color: #e6b800;
    }
    
    /* Centrar textos */
    .centered-text {
        text-align: center;
        font-size: 22px;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- JAVASCRIPT CORREGIDO PARA LA LLUVIA ---
# La clave aquí es 'window.parent.document' para salir del iframe
school_rain_js = """
<script>
    function throwSchoolItems() {
        // Usamos window.parent.document para acceder a la ventana principal de Streamlit
        const doc = window.parent.document;
        
        // Emojis escolares
        const emojis = ['✏️', '📚', '🍎', '📏', '📎', '🎓', '📝', '💯'];
        
        const container = doc.createElement('div');
        container.style.position = 'fixed';
        container.style.top = '0';
        container.style.left = '0';
        container.style.width = '100vw';
        container.style.height = '100vh';
        container.style.pointerEvents = 'none'; // Para que no bloquee los clics
        container.style.zIndex = '9999'; // Para que esté encima de todo
        doc.body.appendChild(container);

        // Estilos de animación
        const styleSheet = doc.createElement("style");
        styleSheet.innerText = `
            @keyframes fallRotate {
                0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
                100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
            }
            .school-item {
                position: absolute;
                top: -10vh;
            }
        `;
        doc.head.appendChild(styleSheet);

        // Crear 50 elementos
        for (let i = 0; i < 50; i++) {
            const item = doc.createElement('div');
            item.classList.add('school-item');
            item.innerText = emojis[Math.floor(Math.random() * emojis.length)];
            
            // Aleatoriedad
            const size = Math.random() * 30 + 20; // Tamaño entre 20 y 50px
            item.style.fontSize = size + 'px';
            item.style.left = Math.random() * 100 + 'vw';
            
            const duration = Math.random() * 3 + 4; // Duración entre 4 y 7 seg
            item.style.animation = `fallRotate ${duration}s linear forwards`;
            item.style.animationDelay = Math.random() * 5 + 's';

            container.appendChild(item);
        }
        
        // Limpiar todo después de 10 segundos
        setTimeout(() => { 
            container.remove(); 
            styleSheet.remove();
        }, 10000);
    }

    // Ejecutar
    throwSchoolItems();
</script>
"""

# --- CONTENIDO VISUAL ---

st.markdown("<h1 style='text-align: center; border: none;'>✨ 🍎 📚 ✏️ ✨</h1>", unsafe_allow_html=True)
st.title("¡Feliz Cumpleaños!")
st.markdown("<h2 style='text-align: center; margin-top: -20px;'>Sra. Flor</h2>", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<div class="centered-text">
    <p>Que tenga un lindo día, la quiero mucho.</p>
    <br>
    <p style="font-size: 40px;">🎓❤️🎉</p>
</div>
""", unsafe_allow_html=True)

# --- BOTÓN CENTRADO ---
col_izq, col_centro, col_der = st.columns([1, 3, 1])

with col_centro:
    presionado = st.button("Presione para borrar la pizarra 🧽")

if presionado:
    st.balloons() # Globos normales
    # Ejecutamos el script corregido
    components.html(school_rain_js, height=0, width=0)
    st.success("¡Muchas felicidades!")