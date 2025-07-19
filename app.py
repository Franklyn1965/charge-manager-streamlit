import streamlit as st
import time

st.set_page_config(page_title="Sistema de Carga de Baterías", layout="wide")
st.title("🔋 Sistema de Carga de Baterías")

# 🧠 Inicializar estado
if "cliente_confirmado" not in st.session_state:
    st.session_state.cliente_confirmado = False
if "nombre" not in st.session_state:
    st.session_state.nombre = ""
if "telefono" not in st.session_state:
    st.session_state.telefono = ""
if "cantidad" not in st.session_state:
    st.session_state.cantidad = 1
if "estado_baterias" not in st.session_state:
    st.session_state.estado_baterias = {}

# 📋 Formulario del cliente
if not st.session_state.cliente_confirmado:
    with st.form("formulario_cliente"):
        nombre = st.text_input("Nombre del cliente")
        telefono = st.text_input("Teléfono")
        cantidad = st.slider("Cantidad de baterías", 1, 5, 1)
        enviado = st.form_submit_button("Registrar")

        if enviado and nombre and telefono:
            st.session_state.nombre = nombre
            st.session_state.telefono = telefono
            st.session_state.cantidad = cantidad
            st.session_state.cliente_confirmado = True
            st.rerun()
        elif enviado:
            st.warning("Por favor, completa nombre y teléfono.")
else:
    nombre = st.session_state.nombre
    telefono = st.session_state.telefono
    cantidad = st.session_state.cantidad

    st.subheader(f"🧾 Cliente: {nombre} ({telefono})")

    for i in range(cantidad):
        st.markdown("---")
        st.subheader(f"🔋 Batería {i+1}")

        col1, col2 = st.columns(2)
        with col1:
            marca = st.text_input(f"Marca", key=f"marca_{i}")
        with col2:
            modelo = st.text_input(f"Modelo", key=f"modelo_{i}")

        if f"btn_{i}" not in st.session_state.estado_baterias:
            st.session_state.estado_baterias[f"btn_{i}"] = "Pendiente"

        estado = st.empty()
        if st.button(f"Iniciar carga Batería {i+1}", key=f"btn_{i}"):
            inicio = time.strftime("%H:%M:%S")
            estado.markdown(f"🕒 Inicio: {inicio}<br>Marca: {marca}<br>Modelo: {modelo}", unsafe_allow_html=True)
            for seg in range(10, -1, -1):  # puedes cambiar a 3600 para una hora real
                estado.markdown(f"⏳ Tiempo restante: <strong>{seg} segundos</strong>", unsafe_allow_html=True)
                time.sleep(1)
            estado.markdown("✅ <strong>Carga completada</strong>", unsafe_allow_html=True)
            st.audio(data=b'\x00' * 5000, format="audio/wav")  # sonido simulado
            st.session_state.estado_baterias[f"btn_{i}"] = "Completada"

    st.success("Carga en curso. Puedes actualizar datos si lo deseas.")
    if st.button("➕ Atender otro cliente"):
        st.session_state.cliente_confirmado = False
        st.session_state.nombre = ""
        st.session_state.telefono = ""
        st.session_state.cantidad = 1
        st.session_state.estado_baterias = {}
        st.rerun()
