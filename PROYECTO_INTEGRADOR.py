# -*- coding: utf-8 -*-
"""
Created on Tue May  9 15:11:33 2023

@author: camac
"""

import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd # Importacion estandar de la libreria Pandas
import numpy  as np # Importacion estandar de la libreria NumPy


st.set_page_config(
    page_title="FIBRA EN LA USTA",
    page_icon="👋",
)

st.write("# :red[Despliegue de fibra en la USTA]🚀 ")

st.sidebar.success("SANTIAGO JOSE HERRERA TORRES")

st.markdown("""<p style='text-align: justify;'>En un entorno digital en constante evolución, la demanda de ancho de banda y la necesidad de una conectividad robusta están en aumento. 
    En este contexto, la fibra óptica GPON se presenta como una solución tecnológica de vanguardia que ofrece velocidades de Internet ultra 
    rápidas, baja latencia y una infraestructura capaz de satisfacer las necesidades presentes y futuras de comunicación. Esta red de fibra 
    óptica no solo mejora la calidad de vida de los residentes, sino que también impulsa el desarrollo económico al proporcionar una base sólida
    para las empresas y la innovación tecnológica.<br></br></p>""",unsafe_allow_html=True)

st.write("# :blue[Nuestros objetivos]🎯🎯")
st.markdown("""
            - Presentar la Visión Estratégica
            - Desglose del Presupuesto
            - Mapeo de la Red
            """)    
        
st.write("# :blue[El despliegue de fibra óptica se realizará en dos fases:]")
st.subheader("Fase 1:")
st.markdown("""
                - Se realizará un estudio de las rutas óptimas para la instalación de la fibra óptica.
                - Se adquirirá el material necesario para el despliegue.
                - Se obtendrán los permisos necesarios para realizar las obras.
            """)
st.subheader("Fase 2:")
st.markdown("""
            - Se instalará la fibra óptica en las rutas definidas.
            - Se conectarán las sedes universitarias al punto de acceso central.
            - Se realizarán pruebas de funcionamiento para garantizar la calidad del servicio.
            """)

url = 'https://www.canva.com/design/DAFh6JsOnuw/dA69ZHOLgPihR0HQ91bjaA/edit?utm_content=DAFh6JsOnuw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'


