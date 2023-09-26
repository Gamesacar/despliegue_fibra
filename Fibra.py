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
import matplotlib.pyplot as plt
from PIL import Image


st.set_page_config(
    page_title="FIBRA EN LA USTA",
    page_icon="📡",
)

st.write("# :red[Despliegue de fibra en la USTA]🚀 ")

st.sidebar.success("SANTIAGO JOSE HERRERA TORRES")

st.markdown("""<p style='text-align: justify;'>En un entorno digital en constante evolución, la demanda de ancho de banda y la necesidad de una conectividad robusta están en aumento. 
    En este contexto, la fibra óptica GPON se presenta como una solución tecnológica de vanguardia que ofrece velocidades de Internet ultra 
    rápidas, baja latencia y una infraestructura capaz de satisfacer las necesidades presentes y futuras de comunicación. Esta red de fibra 
    óptica no solo mejora la calidad de vida de los residentes, sino que también impulsa el desarrollo económico al proporcionar una base sólida
    para las empresas y la innovación tecnológica.<br></br></p>""",unsafe_allow_html=True)

# Leyenda
st.subheader(" :blue[**Implementación de la fibra óptica en Colombia**]")
st.markdown("""<p style='text-align:justify;'> El crecimiento de la fibra óptica en Colombia
            tiene un impacto positivo en 
            el desarrollo económico y social del país. La fibra óptica permite ofrecer 
            servicios de internet de alta velocidad a un mayor número de personas, lo que
            facilita el acceso a la educación, la salud y otros servicios. Además, la fibra
            óptica contribuye a la creación de empleo y al desarrollo
            de nuevas empresas.</br></br>A continuacion el gráfico muestra el crecimiento de la 
            implementación de la fibra óptica en Colombia en los últimos años</p>""",unsafe_allow_html=True)

# Datos
data = pd.DataFrame({
    "Año": [2017, 2018, 2019, 2020, 2021, 2022],
    "Kilometros de Fibra Óptica": [18.000, 22.000, 26.000, 30.000, 34.000, 38.000],
    "colors":['#00FFFF', '#00FFFF', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']
})

st.bar_chart(data=data, x="Año", y="Kilometros de Fibra Óptica", color="colors")




st.write("# :blue[Nuestros objetivos]🎯🎯")
st.markdown("""<p>
            🔴 Presentar la Visión Estratégica <br></br>
            🟢 Desglose del Presupuesto <br></br>
            🟡 Mapeo de la Red
            </p>
            """,unsafe_allow_html=True)    
        
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

st.write("# :blue[¿Que es una fibra GPON?]")

st.markdown("""<p style='text-align:justify;'> Las redes GPON están compuestas por
            diferentes equipos para llevar la conexión a la red y a Internet por la
            fibra óptica</p>""",unsafe_allow_html=True)
            
gpon = Image.open('gpon.png')
st.image(gpon, caption='Fibra')

st.markdown("""<p style='text-align:justify;'>Primero la OLT (Optical Line Terminal) se conecta 
            al divisor óptico a través de una única fibra óptica, y después el divisor óptico se
            conectará a las ONU/ ONT. Después GPON adoptará WDM para transmitir datos de 
            diferentes longitudes de onda ascendentes / descendentes sobre el mismo ODN.
            Las longitudes de onda oscilarán entre 1290-1330 nm en la dirección de subida
            y de 1480 – 1500 nm en dirección de descarga</p>""",unsafe_allow_html=True)
            

st.write("# :blue[Limitantes de distancia]")
st.markdown("""<p>
            🔴 Alcance lógico máximo: 60 km <br></br>
            🟢 Distancia máxima de fibra entre los puntos de envío / recepción (S / R) y de recepción / envío (R / S): 20 kmo <br></br>
            🟡 Tasa: 1.24416 Gbps de subida, 2.48832 Gbps de descarga
            </p>
            """,unsafe_allow_html=True)        



