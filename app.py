import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="¡Feliz Cumpleaños Sra. Flor!",
    page_icon="🍎",
    layout="centered"
)

# Estilos CSS para el TEMA ESCUELA (Pizarra)
st.markdown("""
    <style>
    /* Fondo verde pizarra */
    .stApp {
        background-color: #2b4e3e;
    }
    
    /* Texto color tiza (blanco roto) */
    h1, h2, h3, p, div, span {
        color: #f0f0f0 !important;
        font-family: 'Courier New', Courier, monospace; /* Fuente tipo máquina/escolar */
    }
    
    /* El título principal */
    h1 {
        text-align: center;
        border-bottom: 2px solid #f0f0f0; /* Línea de tiza subrayada */
        padding-bottom: 10px;
    }
    
    /* Estilo del botón */
    .stButton>button {
        width: 100%;
        background-color: #ffcc00; /* Amarillo tiza/resaltador */
        color: #2b4e3e; /* Texto oscuro para contraste */
        border: 2px solid #ffffff;
        border-radius: 5px;
        font-weight: bold;
        font-size: 18px;
    }
    
    /* Centrar textos */
    .centered-text {
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA APP ---

# Decoración superior
st.markdown("<h1 style='text-align: center;'>🍎 📚 ✏️</h1>", unsafe_allow_html=True)

# Título
st.title("¡Feliz Cumpleaños!")
st.markdown("<h2 style='text-align: center;'>Sra. Flor</h2>", unsafe_allow_html=True)

st.write("") # Espacio vacío

# El Mensaje
st.markdown("""
<div class="centered-text">
    <p>Que tenga un lindo día, la quiero mucho.</p>
    <p>🎓</p>
</div>
""", unsafe_allow_html=True)

st.write("") 
st.write("") 
st.write("") 

# Botón sorpresa
if st.button("Presione para borrar la pizarra 🧽"):
    st.balloons()  # Globos de celebración
    st.success("¡Muchas felicidades!")
    
    # Un pequeño efecto extra: nieve (como polvo de tiza)
    time.sleep(1)
    st.snow()