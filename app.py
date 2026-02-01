import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="¡Feliz Cumpleaños!", page_icon="🎂", layout="centered")

# Estilos CSS para centrar y dar formato bonito en el celular
st.markdown("""
    <style>
    .stApp {
        background-color: #FFEFD5;
    }
    h1 {
        color: #d63384;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    p {
        font-size: 18px;
        color: #333333;
        text-align: center;
    }
    .stButton>button {
        width: 100%;
        background-color: #d63384;
        color: white;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título y Mensaje
st.title("🎉 ¡Feliz Cumpleaños! 🎉")
st.subheader("Para la Profe más genial")

st.write("---")

st.markdown("""
<div style="text-align: center;">
    <p>Le deseamos un día lleno de alegría, descanso y mucha felicidad.</p>
    <p>Gracias por su paciencia y dedicación.</p>
    <p>🎂🎁🎈</p>
</div>
""", unsafe_allow_html=True)

# Espacio
st.write("") 
st.write("") 

# Botón sorpresa
if st.button("Presione aquí para una sorpresa 🎁"):
    st.balloons()  # Lanza globos
    st.success("¡Que tenga un excelente día!")
    time.sleep(1)
    st.snow()      # Lanza confeti/nieve