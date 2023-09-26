import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Presupuesto general",
    page_icon="📡",
)
st.write("# :orange[PRESUPUESTO GENERAL DEL PROYECTO] 📝💵 ")


st.markdown("""<p style='text-align: justify;'>
Como ingeniero de telecomunicaciones, mi objetivo es proporcionar un servicio de internet de 
alta velocidad y confiabilidad a las universidades de Bucaramanga, Floridablanca y Piedecuesta
. Para ello, realizaré un despliegue de fibra óptica que conecte las cuatro sedes 
universitarias con un punto de acceso central teniendo en cuenta el siguiente presupuesto.<br></br></p>""",unsafe_allow_html=True)


# Creamos la tabla
equipos = pd.DataFrame([
    ("ODF", "FOCC", "$1000", "Gabinete de distribución de fibra óptica","16 puertos"),
    ("OLT", "Tp-link", "$2500", "Nodo central de fibra óptica"," puertos GPON, 10 Gbps"),
    ("Splitters de fibra óptica", "Huawei", "$500/unidad", "Divisor óptico","1x16, 1x8, 1x4"),
    ("Patch panel", "Huawei", "$500", "Panel de conexión de fibra óptica","16 puertos"),
    ("Cable de fibra óptica", "Huawei", "$700/km", "Cable de fibra óptica para instalación subterránea o aérea","10 Gbps"),
    ("Conectores de fibra óptica", "Huawei", "$10/unidad", "Conectores de fibra óptica para unir los cables de fibra óptica","SC/UPC"),
    ("Cable de conexión", "Huawei", "$5/unidad", "Cable de conexión para conectar los equipos de fibra óptica","SC/UPC a SC/UPC"),
    ("Herramientas de instalación", "Huawei", "$500", "Herramientas para la instalación de fibra óptica","Cortadoras, pelacables y conectores"),
], columns=["Nombre del equipo", "Marca", "Valor", "Descripcion","Características"])

# Agregamos un título a la tabla
st.title("Equipos necesarios para el despliegue de fibra óptica")
equipos = equipos.sort_values(by="Nombre del equipo")

st.markdown("<table class='equipos'>" + equipos.to_html(index=False, escape=False) + "</table>", unsafe_allow_html=True)


st.subheader(" :blue[**Detalles adicionales:**]")
st.markdown("""<p style='text-align: justify;'>La topología adecuada para el despliegue de fibra óptica para las
            universidades de Bucaramanga, Floridablanca y Piedecuesta es la topología estrella. Esta topología es la más adecuada para
            redes FTTH, ya que permite conectar a cada usuario de forma individual a la red</p>""",unsafe_allow_html=True)
image = Image.open('toplogia.png')
st.image(image, caption='Ejemplo topologia estrella')
            
st.markdown("""<p>
            🔴 Las universidades tienen una gran cantidad de usuarios, por lo que la topología estrella permite conectar a cada usuario de forma individual.<br></br>
            🟢 Las universidades están ubicadas en tres ciudades diferentes, por lo que la topología estrella permite conectarlas de forma eficiente<br></br>
            🟡 La topología estrella es la más fácil de administrar y mantener, lo que es importante para una red de gran tamaño<br></br>
            🟣 La red se puede escalar fácilmente agregando más nodos centrales o splitters
            </p>
            """,unsafe_allow_html=True) 

sedes = [
    {
        "Sede": "Bucaramanga",
        "Componentes": [
            "Nodo central de fibra óptica	: 8 puertos GPON: Tp-link",
            "Splitters de fibra óptica	: Splitter-1x16	:Huawei",
            "Cables de fibra óptica	: Cable-Fibra-Optica-10G-Monomodo	:Huawei",
        ],
    },
    {
        "Sede": "Floridablanca",
        "Componentes": [
            "Nodo central de fibra óptica	: OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica	: Splitter-1x8	 :Huawei",
            "Cables de fibra óptica: Cable-Fibra-Optica-10G-Monomodo:Corning",
        ],
    },
    {
        "Sede": "Piedecuesta",
        "Componentes": [
            "Nodo central de fibra óptica	: OLT-GPON-8:Tp-link",
            "Splitters de fibra óptica	: Splitter-1x4	:Huawei",
            "Cables de fibra óptica: Cable-Fibra-Optica-10G-Monomodo	: Corning",
        ],
    },
    {
        "Sede": "Limonal",
        "Componentes": [
            "Nodo central de fibra óptica	: OLT-GPON-8:Tp-link",
            "Splitters de fibra óptica	: Splitter-1x4	:Huawei",
            "Cables de fibra óptica: Cable-Fibra-Optica-10G-Monomodo :Corning",
        ],
    },
]

st.write("# :blue[componentes por sede]")

sede_seleccionada = st.selectbox("Seleccione una sede:", [info["Sede"] for info in sedes])

# Buscar información de la sede seleccionada
sede_info = next((info for info in sedes if info["Sede"] == sede_seleccionada), None)

if sede_info:
    st.write(f"## {sede_info['Sede']}")
    
    # Crear una tabla con tres columnas: Nombre, Valor, Marca
    tabla_info_componentes = [
        ["Nombre", "Valor", "Marca"]
    ]
    
    for componente in sede_info["Componentes"]:
        nombre, valor, marca = [info.strip() for info in componente.split(":")]
        tabla_info_componentes.append([nombre, valor, marca])
    
    # Mostrar la tabla
    st.table(tabla_info_componentes)
else:
    st.write("Seleccione una sede para ver sus componentes.")
    
button = st.button("Ir a la página web", url="https://www.ztocable.com/product-category/fiber-optic-cable?keyword=optic%20cable&placement=&gclid=CjwKCAjwgsqoBhBNEiwAwe5w0ztIErlIRxEKViRyX5mzXD5O2cV8lr7BogEncBVPwShgefx6BoCcRgQAvD_BwE")

# Estilo del botón

button.style({
    "backgroundColor": "#0000FF",
    "color": "#FFFFFF",
    "fontSize": 20,
    "fontWeight": "bold",
    "borderRadius": 5,
    "width": "200px",
    "height": "50px",
})    