# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:32:07 2023

@author: camac
"""
import folium
import streamlit as st
from streamlit_folium import st_folium
from PIL import Image
import folium 


st.set_page_config(
    page_title="Despliegue de RED GPON",
    page_icon="👋",
)

st.write("# :red[MAPA DE DESPLIEGUE]🚀🚀🚀 ")


st.markdown("""<p style='text-align: justify;'>Una vez instalada la fibra óptica, 
            se conectarán las sedes universitarias al punto de acceso central. Para 
            ello, se utilizarán conectores especiales que permiten unir los cables 
            de fibra óptica.<br></br></p>""",unsafe_allow_html=True)

            

# Crear un mapa de Folium
m = folium.Map(location=[7.137061040191279, -73.12805527231112], zoom_start=14)
image = Image.open('Diseño.png')

# Definir información de las sedes
locations = [
    {
        'name': 'Sede Bucaramanga',
        'lat': 7.137061040191279,
        'lon': -73.12805527231112,
        'description': 'Esta es la Sede Bucaramanga.',
        'image_path': Image.open('Diseño.png')
    },
    {
        'name': 'Sede Floridablanca',
        'lat': 7.065556432696987,
        'lon': -73.09531850115162,
        'description': 'Esta es la Sede Floridablanca.',
        'image_path': Image.open('Diseño.png')
    },
    {
        'name': 'Sede Piedecuesta',
        'lat': 7.022842715565784,
        'lon': -73.05940429202747,
        'description': 'Esta es la Sede Piedecuesta.',
        'image_path': Image.open('Diseño.png')
    },
    {
        'name': 'Sede Limonal',
        'lat': 7.008073410481673,
        'lon': -73.05142322999137,
        'description': 'Esta es la Sede Limonal.',
        'image_path':Image.open('Diseño.png')
    }
]

# Coordenadas de la ruta de la fibra óptica (Bucaramanga -> Floridablanca -> Piedecuesta -> Limonal)
fibra_optica_route = [(7.137061040191279, -73.12805527231112),
                      (7.065556432696987, -73.09531850115162),
                      (7.022842715565784, -73.05940429202747),
                      (7.008073410481673, -73.05142322999137)]

cell_tower = {

    'coverage_radius': 60,  # Radio de cobertura en metros
    'num_sides': 6,  # Número de lados del polígono (forma de panal)
    'border_color': 'green',  # Color del borde del marcador
    'fill_color': 'green',  # Color del relleno del marcador
    'fill_opacity': 0.2  # Opacidad del relleno del marcador
}
# Agregar marcadores con información personalizada y color naranja
for location in locations:
    folium.Marker(
        location=[location['lat'], location['lon']],
        icon=folium.Icon(color='orange'),  # Cambiar el color del marcador a naranja
        popup=folium.Popup(location['description'], max_width=2200),  # Descripción personalizada
        tooltip=location['name']
    ).add_to(m)


for coord in fibra_optica_route:
    folium.RegularPolygonMarker(
        location=coord,
        number_of_sides=cell_tower['num_sides'],  # Número de lados (forma de panal)
        radius=cell_tower['coverage_radius'],  # Radio de cobertura
        color=cell_tower['border_color'],  # Color del borde del marcador
        fill_color=cell_tower['fill_color'],  # Color del relleno del marcador
        fill_opacity=cell_tower['fill_opacity']  # Opacidad del relleno del marcador
    ).add_to(m)

# Trazar la ruta de la fibra óptica en el mapa
folium.PolyLine(locations=fibra_optica_route, color='blue', weight=3).add_to(m)

# Llamar a la función para renderizar el mapa de Folium en Streamlit
st_data = st_folium(m, width=1000)

