import streamlit as st
import numpy as np
import pandas as pd
import scipy.stats as stats
import plotly.graph_objects as go
import sympy as sp

from io import BytesIO
from datetime import datetime


st.set_page_config(page_title="Calculadora", layout="wide", initial_sidebar_state="expanded")


st.markdown("""
<style>

    .main-title {font-size: 42px; font-weight: 800; color: #2563EB; letter-spacing: 2px;}

    .subtitle {font-size: 17px;color: #94A3B8;}

    .section-title {font-size: 23px; font-weight: 700;}

    div[data-testid="stMetric"] {background-color: rgba(128,128,128,0.08); padding: 18px; border-radius: 12px;}

</style>
""", unsafe_allow_html=True)


st.sidebar.title("Calculadora")

st.sidebar.caption("Calculadora de Productos Financieros Derivados")

st.sidebar.divider()

menu = st.sidebar.radio("NAVEGACIÓN", ["Inicio", "Valor del dinero", "Forward y Futures", "Opciones financieras", "Estrategias con opciones", 
                                       "Arbitraje", "Modelo binomial", "Griegas", "Swaps", "Reportes"])

st.sidebar.divider()

st.sidebar.caption("Proyecto académico")
st.sidebar.caption("Versión 1.0")


if menu == "Inicio":

    st.markdown(
        '<p class="main-title">DERIVACALC</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">'
        'Plataforma integral de valuación de instrumentos '
        'financieros derivados'
        '</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.subheader("Bienvenido a DerivaCalc")

    st.write("""
    Esta plataforma permite realizar cálculos financieros,
    analizar instrumentos derivados y comprender los
    procedimientos matemáticos utilizados en su valuación.
    """)



    col1, col2, col3 = st.columns(3)

    col1.metric("Módulos disponibles", "9")
    col2.metric("Lenguaje", "Python")
    col3.metric("Plataforma", "Streamlit")

    st.divider()

    st.subheader("Módulos de la calculadora")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("###  Valor del dinero")
        st.write("Valor presente, valor futuro y tasas de interés.")

        st.markdown("###  Forward y Futures")
        st.write("Valuación de contratos y posiciones financieras.")

        st.markdown("###  Opciones financieras")
        st.write("Opciones Call, Put y sus componentes.")

        st.markdown("###  Arbitraje")
        st.write("Paridad Put-Call y oportunidades de arbitraje.")

    with col2:

        st.markdown("### 📈 Estrategias con opciones")
        st.write("Combinaciones de posiciones y resultados.")

        st.markdown("###  Modelo binomial")
        st.write("Árboles de precios y valuación de opciones.")

        st.markdown("###  Griegas")
        st.write("Medidas de riesgo de las opciones.")

        st.markdown("###  Swaps")
        st.write("Flujos y valuación de contratos Swap.")

    st.divider()

    st.info(
        "Selecciona cualquiera de los módulos en el menú "
        "lateral para comenzar."
    )



else:

    st.title(menu)

    st.info(
        f"El módulo de {menu} se encuentra en desarrollo."
    )

    st.caption("DerivaCalc | Proyecto académico")
