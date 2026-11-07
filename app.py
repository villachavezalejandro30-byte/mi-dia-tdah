
import streamlit as st
from datetime import date

st.title("Mi Día - TDAH")

st.header("Plan de hoy")
plan = [
    {"nombre": "Buscar trabajo", "duracion": 50},
    {"nombre": "Inglés", "duracion": 50},
    {"nombre": "Gimnasio", "duracion": 60},
]
for actividad in plan:
    st.write("- ", actividad["nombre"], "-", actividad["duracion"], "minutos")

st.header("Enfoque")
duracion = st.selectbox("Duración de enfoque en minutos", [25, 45, 50, 60, 90], index=2)
descanso = st.selectbox("Descanso en minutos", [5, 10, 15])
st.write("Vas a enfocarte", duracion, "minutos y descansar", descanso, "minutos.")

st.header("Diario")
hoy = st.date_input("Fecha", date.today())
animo = st.selectbox("¿Cómo te sientes hoy?", ["Feliz", "Tranquilo", "Cansado", "Ansioso", "Motivado"])
texto = st.text_area("Escribe cómo te sientes hoy:")
if st.button("Guardar entrada del diario"):
    st.write("Guardado:", hoy, "-", animo)

st.header("Lugares")
lugar = st.text_input("¿Qué lugar nuevo visitaste?")
fecha_lugar = st.date_input("Fecha del lugar", date.today())
if st.button("Guardar lugar"):
    st.write("Guardado:", lugar)

st.header("Lectura")
libro = st.text_input("¿Qué libro estás leyendo?")
estado = st.selectbox("Estado del libro", ["Por leer", "Leyendo", "Terminado"])
paginas = st.number_input("Páginas leídas", min_value=0, step=10)
if st.button("Guardar libro"):
    st.write("Guardado:", libro, "-", estado, "-", paginas, "páginas")

st.header("Notas")
nota = st.text_area("Escribe una nota rápida:")
if st.button("Guardar nota"):
    st.write("Nota guardada:", nota)
