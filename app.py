import streamlit as st
import time

st.set_page_config(page_title="Sistema de Carga de Baterías", layout="wide")

st.title("🔋 Sistema de Carga de Baterías")

# Formulario de cliente
with st.form("formulario_cliente"):
    nombre = st.text_input("Nombre del cliente")
    telefono = st.text_input("Teléfono")
    cantidad = st.slider("Cantidad de baterías", 1, 5, 1)
    enviado = st.form_submit_button("Registrar")

# Procesar datos si se envió el formulario
if enviado and nombre and telefono:
    st.subheader(f"🧾 Cliente: {nombre} ({telefono})")
    
    for i in range(cantidad):
        st.markdown(f"---")
        st.subheader(f"🔋 Batería {i+1}")
        marca = st.text_input(f"Marca", key=f"marca_{i}")
        modelo = st.text_input(f"Modelo", key=f"modelo_{i}")
        
        placeholder = st.empty()
        if st.button(f"Iniciar carga Batería {i+1}", key=f"btn_{i}"):
            inicio = time.strftime("%H:%M:%S")
            st.write(f"🕒 Inicio: {inicio} | Marca: {marca} | Modelo: {modelo}")
            for seg in range(10, -1, -1):
                placeholder.markdown(f"⏱️ Tiempo restante: **{seg} segundos**")
                time.sleep(1)
            placeholder.markdown("✅ **Carga completada**")
            st.audio(data=b'\x00' * 5000, format="audio/wav")  # sonido simulado

    st.success("Cliente procesado. Puedes registrar otro sin esperar que las cargas terminen.")
elif enviado:
    st.warning("Por favor, llena nombre y teléfono para continuar.")
