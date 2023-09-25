# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import folium
import streamlit as st
from streamlit_folium import st_folium
from PIL import Image


st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="📡",
)

st.write("# :red[MAPA DE DESPLIEGUE]🚀🚀🚀 ")


st.markdown("""<p style='text-align: justify;'>Una vez instalada la fibra óptica, 
            se conectarán las sedes universitarias al punto de acceso central. Para 
            ello, se utilizarán conectores especiales que permiten unir los cables 
            de fibra óptica.<br></br></p>""",unsafe_allow_html=True)

images = ['Bucaramanga.jpeg',
          'Floridablanca.jpeg',
          'Piedecuesta.jpeg',
          'Limonal.jpeg']

# Mostrar las imágenes en una disposición en mosaico
image_index = st.slider('Sedes en donde se desplegara el servicio', 0, len(images)-1)

# Mostrar la imagen seleccionada
st.image(images[image_index], use_column_width=True)
            

# Crear un mapa de Folium
m = folium.Map(location=[7.137061040191279, -73.12805527231112], zoom_start=14)
image = Image.open('Diseño.png')

st.markdown("""<p style='text-align: justify;'>Graficamente se puede observar en el 
            siguiente mapa el despliegue, la cobertura que tendra el servicio,
            los componentes utilizados y la posible ruta que tomara la fibra optica
            a las diferentes sedes<br></br></p>""",unsafe_allow_html=True)
# Definir información de las sedes
sedes = [
    {
        "Sede": "Bucaramanga",
        "Lat": 7.136866984518489,
        "Lon": -73.12829163907617,
        "Componentes": [
            "Nodo central de fibra óptica : 8 puertos GPON : Tp-link",
            "Splitters de fibra óptica : Splitter-1x16 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Huawei",
        ],
    },
    {
        "Sede": "Floridablanca",
        "Lat": 7.065556432696987,
        "Lon": -73.09531850115162,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x8 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Sede": "Piedecuesta",
        "Lat": 7.022842715565784,
        "Lon": -73.05940429202747,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x4 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Sede": "Limonal",
        "Lat": 7.008073410481673,
        "Lon": -73.05142322999137,
        "Componentes": [
            "Nodo central de fibra óptica : OLT-GPON-8 : Tp-link",
            "Splitters de fibra óptica : Splitter-1x4 : Huawei",
            "Cables de fibra óptica : Cable-Fibra-Optica-10G-Monomodo : Corning",
        ],
    },
    {
        "Sede": "MOVISTAR",
        "Lat": 7.118167921369244,
        "Lon": -73.12671126865293,
        "Componentes": [
            "Un ISP es una empresa que proporciona conectividad a Internet a los usuarios",
        ],
    },
]

# Coordenadas de la ruta de la fibra óptica (Bucaramanga -> Floridablanca -> Piedecuesta -> Limonal)
fibra_optica_route = [(7.136866984518489, -73.12829163907617),
                      (7.065556432696987, -73.09531850115162),
                      (7.022842715565784, -73.05940429202747),
                      (7.008073410481673, -73.05142322999137)]

cell_tower = {

    'coverage_radius': 1000,  # Radio de cobertura en metros
    'num_sides': 6,  # Número de lados del polígono (forma de panal)
    'border_color': 'green',  # Color del borde del marcador
    'fill_color': 'green',  # Color del relleno del marcador
    'fill_opacity': 0.2  # Opacidad del relleno del marcador
}
# Agregar marcadores con información personalizada y color naranja


for sede in sedes:
    sede_html = f"<b>{sede['Sede']}</b><br>"
    for componente in sede['Componentes']:
        sede_html += f"- {componente}<br>"
    
    folium.Marker(
        location=[sede['Lat'], sede['Lon']],
        icon=folium.Icon(color='orange'),  # Cambiar el color del marcador a naranja
        popup=folium.Popup(sede_html, max_width=300),
        tooltip=sede['Sede']
    ).add_to(m)


for coord in fibra_optica_route:
    folium.Circle(
        location=coord,
        radius=cell_tower['coverage_radius'],  # Radio de cobertura
        number_of_sides=cell_tower['num_sides'],  # Número de lados (forma de panal)
        color=cell_tower['border_color'],  # Color del borde del marcador
        fill_color=cell_tower['fill_color'],  # Color del relleno del marcador
        fill_opacity=cell_tower['fill_opacity']  # Opacidad del relleno del marcador
    ).add_to(m)

# Trazar la ruta de la fibra óptica en el mapa
folium.PolyLine(locations=fibra_optica_route, color='blue', weight=3).add_to(m)

# Llamar a la función para renderizar el mapa de Folium en Streamlit
st_data = st_folium(m, width=1000)

