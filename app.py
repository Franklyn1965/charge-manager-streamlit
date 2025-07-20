import streamlit as st
import time

st.set_page_config(page_title="Sistema de Carga de Baterías", layout="wide")
st.title("🔋 Sistema de Carga de Baterías")

# 🧠 Inicializar variables de estado
st.session_state.setdefault("cliente_confirmado", False)
st.session_state.setdefault("nombre", "")
st.session_state.setdefault("telefono", "")
st.session_state.setdefault("cantidad", 1)
st.session_state.setdefault("estado_baterias", {})
st.session_state.setdefault("reiniciar", False)

# 🔄 Si se solicitó reinicio, limpiar estado
if st.session_state.reiniciar:
    st.session_state.cliente_confirmado = False
    st.session_state.nombre = ""
    st.session_state.telefono = ""
    st.session_state.cantidad = 1
    st.session_state.estado_baterias = {}
    st.session_state.reiniciar = False
    st.experimental_rerun()

# 📋 Formulario de cliente
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
            st.experimental_rerun()
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
        marca = col1.text_input("Marca", key=f"marca_{i}")
        modelo = col2.text_input("Modelo", key=f"modelo_{i}")

        if f"estado_{i}" not in st.session_state.estado_baterias:
            st.session_state.estado_baterias[f"estado_{i}"] = "Pendiente"

        estado = st.empty()
        if st.button(f"Iniciar carga Batería {i+1}", key=f"btn_{i}"):
            inicio = time.strftime("%H:%M:%S")
            estado.markdown(f"🕒 Inicio: {inicio}<br>Marca: {marca}<br>Modelo: {modelo}", unsafe_allow_html=True)
            for seg in range(10, -1, -1):  # Para prueba; cambia a 3600 para 1 hora
                estado.markdown(f"⏳ Tiempo restante: <strong>{seg} segundos</strong>", unsafe_allow_html=True)
                time.sleep(1)
            estado.markdown("✅ <strong>Carga completada</strong>", unsafe_allow_html=True)
            st.session_state.estado_baterias[f"estado_{i}"] = "Completada"

    st.success("Todas las cargas activas. Puedes atender otro cliente cuando gustes.")
    
    if st.button("➕ Atender otro cliente"):
        st.session_state.reiniciar = True
