import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd

st.write("# :orange[PRESUPUESTO GENERAL DEL PROYECTO] 📝💵 ", align="center", style={"background-color": "#FF8C00"})


st.markdown("""<p style='text-align: justify;'>
Como ingeniero de telecomunicaciones, mi objetivo es proporcionar un servicio de internet de 
alta velocidad y confiabilidad a las universidades de Bucaramanga, Floridablanca y Piedecuesta
. Para ello, realizaré un despliegue de fibra óptica que conecte las cuatro sedes 
universitarias con un punto de acceso central teniendo en cuenta el siguiente presupuesto.<br></br></p>""",unsafe_allow_html=True)


# Creamos la tabla
equipos = pd.DataFrame([
    ("ODF", "FOCC", "$200.000", "Gabinete de distribución de fibra óptica"),
    ("Patch panel", "FOCC", "$100.000", "Panel de conexión de fibra óptica"),
    ("Cable de fibra óptica", "FOCC", "$10.000/metro", "Cable de fibra óptica para instalación subterránea o aérea"),
    ("Conectores de fibra óptica", "FOCC", "$5.000/par", "Conectores de fibra óptica para unir los cables de fibra óptica"),
    ("Cable de conexión", "FOCC", "$2.000/metro", "Cable de conexión para conectar los equipos de fibra óptica"),
    ("Herramientas de instalación", "FOCC", "$500.000", "Herramientas para la instalación de fibra óptica"),
], columns=["Nombre del equipo", "Marca", "Valor", "Característica"])

# Agregamos un título a la tabla
st.title("Equipos necesarios para el despliegue de fibra óptica")
equipos = equipos.sort_values(by="Nombre del equipo")

css = """
<style>
table.equipos {
    border-collapse: collapse;
    width: 100%;
    background-color: #0000FF;

}

table.equipos th {
    background-color: #0000FF;
    color: white;
    text-align: center;
    padding: 8px;
}

table.equipos tr:nth-child(even) {
    background-color: #0000FF;
}

table.equipos td {
    padding: 8px;
    text-align: center;
    border-bottom: 1px solid #ddd;
}

table.equipos td:first-child {
    font-weight: bold;
}

</style>
"""

# Aplicar el estilo CSS a la tabla
st.markdown(css, unsafe_allow_html=True)
st.markdown("<table class='equipos'>" + equipos.to_html(index=False, escape=False) + "</table>", unsafe_allow_html=True)




