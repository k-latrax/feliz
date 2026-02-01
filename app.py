import streamlit as st
import streamlit.components.v1 as components

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
        background-image: url("https://www.transparenttextures.com/patterns/blackboard.png"); /* Textura sutil de pizarra */
    }
    
    /* Texto color tiza (blanco roto) */
    h1, h2, h3, p, div, span, label {
        color: #f0f0f0 !important;
        font-family: 'Courier New', Courier, monospace; /* Fuente tipo máquina/escolar */
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5); /* Sombra para efecto tiza */
    }
    
    /* El título principal */
    h1 {
        text-align: center;
        border-bottom: 2px solid #f0f0f0; /* Línea de tiza subrayada */
        padding-bottom: 10px;
    }
    
    /* Estilo del botón */
    .stButton>button {
        width: 100%; /* Ocupa todo el ancho de su columna */
        background-color: #ffcc00; /* Amarillo tiza/resaltador */
        color: #2b4e3e !important; /* Texto oscuro para contraste */
        border: 3px solid #ffffff;
        border-radius: 10px;
        font-weight: bold;
        font-size: 20px;
        padding: 10px 0;
        text-shadow: none; /* Quitamos sombra de tiza al botón */
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

# --- JAVASCRIPT PARA LA LLUVIA ESCOLAR PERSONALIZADA ---
# Este bloque crea la animación de lápices, libros, etc.
school_rain_js = """
<script>
    // Definimos los estilos de la animación caída
    const styleSheet = document.createElement("style");
    styleSheet.type = "text/css";
    styleSheet.innerText = `
    @keyframes fallRotate {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(105vh) rotate(360deg); opacity: 0.7; }
    }
    .school-item {
        position: fixed;
        top: -10vh;
        z-index: 9999;
        pointer-events: none;
    }
    `;
    document.head.appendChild(styleSheet);

    function throwSchoolItems() {
        const emojis = ['✏️', '📚', '🍎', '📏', '📎', '🎓', '📝'];
        const container = document.createElement('div');
        document.body.appendChild(container);

        // Creamos 60 elementos
        for (let i = 0; i < 60; i++) {
            const item = document.createElement('div');
            item.classList.add('school-item');
            item.innerHTML = emojis[Math.floor(Math.random() * emojis.length)];
            
            // Tamaños y posiciones aleatorias
            const size = Math.random() * 25 + 20; // Entre 20px y 45px
            item.style.fontSize = size + 'px';
            item.style.left = Math.random() * 100 + 'vw';
            
            // Duración de caída aleatoria entre 3 y 6 segundos
            const duration = Math.random() * 3 + 3;
            item.style.animation = `fallRotate ${duration}s linear forwards`;
            
            // Un pequeño retraso para que no caigan todos de golpe
            item.style.animationDelay = Math.random() * 2 + 's';

            container.appendChild(item);
        }
        
        // Limpiar los elementos después de que terminen de caer (8 segundos)
        setTimeout(() => { container.remove(); }, 8000);
    }

    // Ejecutar la función inmediatamente
    throwSchoolItems();
</script>
"""

# --- CONTENIDO VISUAL DE LA APP ---

# Decoración superior
st.markdown("<h1 style='text-align: center; border: none;'>✨ 🍎 📚 ✏️ ✨</h1>", unsafe_allow_html=True)

# Título
st.title("¡Feliz Cumpleaños!")
st.markdown("<h2 style='text-align: center; margin-top: -20px;'>Sra. Flor</h2>", unsafe_allow_html=True)

st.write("---") # Una línea separadora estilo tiza

# El Mensaje
st.markdown("""
<div class="centered-text">
    <p>Que tenga un lindo día, la quiero mucho.</p>
    <br>
    <p style="font-size: 40px;">🎓❤️🎉</p>
</div>
""", unsafe_allow_html=True)


# --- BOTÓN CENTRADO Y ACCIÓN ---

# Usamos 3 columnas para centrar el botón. 
# El [1, 3, 1] significa: espacio pequeño a la izq, espacio triple al medio, espacio pequeño a la der.
col_izq, col_centro, col_der = st.columns([1, 3, 1])

with col_centro:
    # El botón ahora está dentro de la columna central
    presionado = st.button("Presione para borrar la pizarra 🧽")

if presionado:
    # 1. Lanzamos globos nativos (siempre quedan bien)
    st.balloons()
    
    # 2. Inyectamos nuestra lluvia personalizada escolar (invisible, solo ejecuta el JS)
    components.html(school_rain_js, height=0, width=0)
    
    # 3. Mensaje de éxito
    st.success("¡Muchas felicidades Profe!")