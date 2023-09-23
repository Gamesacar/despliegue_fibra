import streamlit as st
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd

st.write("# :red[COMPONENTES NECESARIOS] 📝📟 ", align="center", style={"background-color": "#FF8C00"})


st.markdown("""<p style='text-align: justify;'>
El proyecto incluye el despliegue de fibra óptica desde el nodo central hasta los edificios
 de las universidades. La red se dividirá en celdas para facilitar la gestión y el 
 mantenimiento.<br></br></p>""",unsafe_allow_html=True)
 
st.subheader(" :blue[**Equipos necesarios:**]")
st.markdown("""<p>
            🔴 Nodo central de fibra óptica<br></br>
            🟢 DSplitters de fibra óptica<br></br>
            🟡 Cables de fibra óptica<br></br>
            🔴 Herramientas de instalación
            </p>
            """,unsafe_allow_html=True) 

st.subheader(" :orange[**Nodo central de fibra óptica**]")
st.markdown("""<p style='text-align: justify;'> Es un dispositivo que sirve como punto de conexión para la red de fibra óptica.
            El nodo central del proyecto admitirá hasta 16 puertos de entrada y salida, lo que permitirá conectar hasta 16 
            splitters de fibra óptica<br></br></p>""",unsafe_allow_html=True)
 


