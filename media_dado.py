import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constantes
m_dado = 3.5
sd_dado = np.sqrt(17.5 / 6)

# Funciones
def tirar_dado(n):
    return np.random.randint(1, 7, size=n)

def ploteo_media_acumulada(tiradas, media):
    media_acumulada = np.cumsum(tiradas) / np.arange(1, len(tiradas)+1)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Escala lineal
    axes[0].plot(media_acumulada)
    axes[0].axhline(media, color='red', linestyle='--', label='Media teórica')
    axes[0].set_xlabel('Número de tiradas')
    axes[0].set_ylabel('Media acumulada')
    axes[0].set_title('Escala lineal en x')
    axes[0].legend()

    # Escala log10
    axes[1].plot(media_acumulada)
    axes[1].axhline(media, color='red', linestyle='--', label='Media teórica')
    axes[1].set_xlabel('Número de tiradas')
    axes[1].set_ylabel('Media acumulada')
    axes[1].set_title('Escala log10 en x')
    axes[1].set_xscale('log')
    axes[1].legend()

    plt.tight_layout()
    return fig

# Interfaz de Streamlit
st.title("Simulación de la media acumulada de un dado")

# Número de tiradas
n = st.number_input("Ingrese el número de tiradas (n)", min_value=1, value=100, step=1)

# Inicializar estado para las tiradas
if "tiradas" not in st.session_state:
    st.session_state.tiradas = None

col1, col2 = st.columns([1,1])

with col1:
    if st.button("Generar tirada"):
        st.session_state.tiradas = tirar_dado(n)
        
with col2:
    if st.button("Resetear"):
        st.session_state.tiradas = None

# Mostrar plot si hay tiradas
if st.session_state.tiradas is not None:
    fig = ploteo_media_acumulada(st.session_state.tiradas, m_dado)
    st.pyplot(fig)
