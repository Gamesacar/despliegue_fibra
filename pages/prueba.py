import streamlit as st
import folium
from streamlit_folium import st_folium

# Crear un mapa de Folium
m = folium.Map(location=[7.137061040191279, -73.12805527231112], zoom_start=14)

# Definir información de las sedes, incluyendo la descripción de los componentes
sedes = [
    {
        "Sede": "Bucaramanga",
        "Lat": 7.137061040191279,
        "Lon": -73.12805527231112,
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
]

# Agregar marcadores personalizados con descripción de componentes
for sede in sedes:
    sede_html = f"<b>{sede['Sede']}</b><br>"
    for componente in sede['Componentes']:
        sede_html += f"- {componente}<br>"
    
    folium.Marker(
        location=[sede['Lat'], sede['Lon']],
        icon=None,
        popup=folium.Popup(sede_html, max_width=300),
        tooltip=sede['Sede']
    ).add_to(m)

# Llamar a la función para renderizar el mapa de Folium en Streamlit
st_data = st_folium(m, width=1000)