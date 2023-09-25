import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="componentes",
    page_icon="📡",
)
st.write("# :red[COMPONENTES NECESARIOS] 📝📟 ", align="center", style={"background-color": "#FF8C00"})


st.markdown("""<p style='text-align: justify;'>
El proyecto incluye el despliegue de fibra óptica desde el nodo central hasta los edificios
 de las universidades. La red se dividirá en celdas para facilitar la gestión y el 
 mantenimiento.</p>""",unsafe_allow_html=True)
 
st.subheader(" :blue[**Equipos necesarios:**]")
st.markdown("""<p>
            🔴 Nodo central de fibra óptica<br></br>
            🟢 DSplitters de fibra óptica<br></br>
            🟡 Cables de fibra óptica<br></br>
            🟣 Herramientas de instalación
            </p>
            """,unsafe_allow_html=True) 

st.subheader(" :orange[**Nodo central de fibra óptica**]")

st.markdown("""<p style='text-align: justify;'> Es un dispositivo que sirve como punto de conexión para la red de fibra óptica.
            El nodo central del proyecto admitirá hasta 16 puertos de entrada y salida, lo que permitirá conectar hasta 16 
            splitters de fibra óptica<br>
            En el caso específico del proyecto de despliegue de fibra óptica para las universidades de Bucaramanga, Floridablanca y Piedecuesta, 
            se recomienda utilizar una OLT con 8 puertos. Esta cantidad de puertos será suficiente para conectar los 4 splitters de fibra óptica
            y contar con un número de puertos de reserva para esto se utlizara una OLT GPON DeltaStream de 8 puertos PON .La OLT se ubicará en la sede central de las 
            universidades de Bucaramanga, Floridablanca y Piedecuesta. Esta ubicación es la más adecuada 
            para garantizar que la red tenga un rendimiento óptimo y que sea fácil de gestionar</p>""",unsafe_allow_html=True)
            

image = Image.open('olt.jpg')
st.image(image, caption='GPON Optical Line Terminal')

st.write("# :blue[ODN]")

st.markdown("""<p style='text-align: justify;'>La ODN (Optical Distribution Network) es la red de distribución de fibra óptica que conecta 
            el nodo central de fibra óptica con los usuarios. En el caso específico del despliegue de fibra óptica para las universidades
            de Bucaramanga, Floridablanca y Piedecuesta, la ODN estará incluida en los siguientes componentes</p>""",unsafe_allow_html=True)
            

st.subheader(":orange[**Splitters de fibra óptica**]")

st.markdown("""<p style='text-align: justify;'>Los splitters de fibra óptica son componentes que dividen la señal de fibra óptica en 
            varias señales más pequeñas. Se utilizan para conectar múltiples usuarios a la red de fibra óptica<br>
            Los splitters de fibra óptica se dividirán de la siguiente manera:<br><br>
                Sede Bucaramanga: 1 splitter de 1x16 (16 salidas)<br><br>
                Sede Floridablanca: 1 splitter de 1x8 (8 salidas)<br><br>
                Sedes Piedecuesta: 2 splitters de 1x4 (4 salidas)</p>""",unsafe_allow_html=True)
            
splitter = Image.open('splitter.png')
st.image(splitter, caption='Divisor óptico 1x16')

st.subheader(":orange[**ODF**]")

st.markdown("""<p style='text-align: justify;'>El ODF es un dispositivo que organiza y conecta los cables de fibra óptica</p>""",unsafe_allow_html=True)
            
odf = Image.open('odf.jpg')
st.image(odf, caption='ODF de 48 puertos')

st.subheader(":orange[**Fibra optica**]")

st.markdown("""<p style='text-align: justify;'>
La fibra óptica utilizada en el despliegue para las universidades de Bucaramanga, Floridablanca
 y Piedecuesta es de tipo monomodo. La fibra óptica monomodo tiene un núcleo muy pequeño, de solo
 9 micrones de diámetro. Esto permite que la luz viaje por la fibra en un solo modo, lo que reduce 
 la atenuación y permite que la señal viaje distancias más largas</p>""",unsafe_allow_html=True)
            
odf = Image.open('fibra.jpg')
st.image(odf, caption='Fibra monomodo')




# Información sobre los componentes
componentes = [
    {
        "Componente": "Nodo central de fibra óptica",
        "Característica": [
            "Puertos: 8 puertos GPON",
            "Velocidad de transmisión: 10 Gbps",
            "Distancia de transmisión: 100 kilómetros",
            "Alimentación: 12 VDC",
            "Dimensiones: 100 x 100 x 100 mm",
            "Peso: 1 kg",
        ],
    },
    {
        "Componente": "Splitters de fibra óptica",
        "Característica": [
            "Tipo: 1x16, 1x8, 1x4",
            "Núcleo: 9 micrones",
            "Revestimiento: 125 micrones",
            "Pérdida de inserción: <0.3 dB",
            "Pérdida de retorno: <-60 dB",
            "Dimensiones: 100 x 100 x 100 mm",
            "Peso: 0.5 kg",
        ],
    },
    {
        "Componente": "Cables de fibra óptica",
        "Característica": [
            "Tipo: monomodo",
            "Núcleo: 9 micrones",
            "Revestimiento: 125 micrones",
            "Banda de transmisión: 1310-1550 nm",
            "Pérdida de inserción: <0.2 dB/km",
            "Pérdida de retorno: <-50 dB",
            "Dimensiones: 25 mm x 100 m",
            "Peso: 0.5 kg/km",
        ],
    },
    {
        "Componente": "Herramientas de instalación",
        "Característica": [
            "Cortadoras: Cortan los cables de fibra óptica a la longitud deseada.",
            "Pelacables: Quitan la cubierta exterior de los cables de fibra óptica.",
            "Conectores: Conectan los cables de fibra óptica a los dispositivos de la red.",
        ],
    },
    {
        "Componente": "ODF",
        "Característica": [
            "Puertos: 16 puertos",
            "Dimensiones: 400 x 400 x 100 mm",
            "Peso: 5 kg",
        ],
    },
    {
        "Componente": "Patch panel",
        "Característica": [
            "Puertos: 16 puertos",
            "Dimensiones: 400 x 400 x 100 mm",
            "Peso: 5 kg",
        ],
    },
    {
        "Componente": "Conectores",
        "Característica": [
            "Tipo: SC/UPC",
            "Dimensiones: 2.5 mm",
            "Peso: 0.01 kg",
        ],
    },
    {
        "Componente": "Cable de conexión",
        "Característica": [
            "Tipo: SC/UPC a SC/UPC",
            "Longitud: 1 metro",
            "Dimensiones: 2.5 mm x 1 metro",
            "Peso: 0.01 kg",
        ],
    },
]

st.write("# :blue[Datasheets de los componentes]")

componente_seleccionado = st.selectbox("Seleccione un componente:", [info["Componente"] for info in componentes])

# Buscar información del componente seleccionado
componente_info = next((info for info in componentes if info["Componente"] == componente_seleccionado), None)

if componente_info:
    st.write(f"## {componente_info['Componente']}")
    tabla_caracteristicas = [["Característica", "Especificacion"]]
    for caracteristica in componente_info["Característica"]:
        nombre, valor = caracteristica.split(":", 1)
        tabla_caracteristicas.append([nombre.strip(), valor.strip()])
    st.table(tabla_caracteristicas)
else:
    st.write("Seleccione un componente para ver sus características.")