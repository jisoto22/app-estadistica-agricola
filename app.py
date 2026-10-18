from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


DATA_DIR = Path(__file__).resolve().parent / "datos"
CSV_FILES = {
    "Parcelas": "parcelas.csv",
    "Clima mensual": "clima_mensual.csv",
    "Muestra de 10 parcelas": "muestra10.csv",
}

st.set_page_config(
    page_title="Estadística agrícola | Sorgo en Tolú",
    page_icon="🌾",
    layout="wide",
)


@st.cache_data
def cargar_csv(nombre_archivo: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / nombre_archivo)


@st.cache_data
def cargar_metadatos() -> dict[str, object]:
    with (DATA_DIR / "metadatos.json").open(encoding="utf-8") as archivo:
        return json.load(archivo)


for nombre_archivo in (*CSV_FILES.values(), "metadatos.json"):
    if not (DATA_DIR / nombre_archivo).is_file():
        st.error(f"No se encontró el archivo requerido `datos/{nombre_archivo}`.")
        st.stop()

metadatos = cargar_metadatos()
datos = {
    nombre: cargar_csv(nombre_archivo)
    for nombre, nombre_archivo in CSV_FILES.items()
}
parcelas = datos["Parcelas"]

st.sidebar.title("Estadística agrícola")
pagina = st.sidebar.radio("Secciones", ("Inicio", "Datos", "EDA"))

if pagina == "Inicio":
    st.title("Análisis estadístico de parcelas agrícolas")
    st.subheader(f"Cultivo de {metadatos['cultivo']} en {metadatos['municipio']}")
    st.write(
        "Proyecto de Estadística Aplicada con Python para Ingeniería Agrícola "
        "de la Universidad de Sucre."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Cultivo", str(metadatos["cultivo"]))
    col2.metric("Municipio", str(metadatos["municipio"]))
    col3.metric("Parcelas", f"{metadatos['n_parcelas']}")

    st.markdown(
        "Explora los archivos y sus estadísticas descriptivas en **Datos**, "
        "o consulta la distribución y las comparaciones del rendimiento en **EDA**."
    )

elif pagina == "Datos":
    st.title("Datos y estadísticas descriptivas")
    st.write(
        "Selecciona cada conjunto para revisar sus registros, tipos de variables "
        "y resumen estadístico. Los valores ausentes se excluyen de los cálculos "
        "de cada variable."
    )

    for nombre, dataframe in datos.items():
        with st.expander(f"{nombre} ({len(dataframe)} filas)", expanded=True):
            st.dataframe(dataframe, width="stretch")
            st.caption(
                f"{dataframe.shape[0]} filas · {dataframe.shape[1]} columnas · "
                f"{int(dataframe.isna().sum().sum())} valores ausentes"
            )
            st.markdown("**Estadísticas descriptivas**")
            st.dataframe(
                dataframe.describe(include="all").T,
                width="stretch",
            )

else:
    st.title("Análisis Exploratorio de Datos (EDA)")
    st.write(
        "El análisis usa la tabla completa de parcelas. Los gráficos y resúmenes "
        "de rendimiento consideran los registros con rendimiento disponible."
    )

    sns.set_theme(style="whitegrid", palette="Set2")
    rendimiento = parcelas.dropna(subset=["rendimiento"]).copy()

    st.subheader("Rendimiento por parcela")
    rendimiento["orden"] = np.arange(1, len(rendimiento) + 1)
    figura, eje = plt.subplots(figsize=(12, 4))
    sns.lineplot(
        data=rendimiento,
        x="orden",
        y="rendimiento",
        marker="o",
        markersize=4,
        ax=eje,
    )
    eje.set(
        xlabel="Número de parcela (orden del archivo)",
        ylabel="Rendimiento",
        title="Rendimiento observado en cada parcela",
    )
    eje.set_xticks(np.arange(1, len(rendimiento) + 1, 10))
    st.pyplot(figura, width="stretch")
    plt.close(figura)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribución del rendimiento")
        figura, eje = plt.subplots(figsize=(7, 4))
        sns.histplot(data=rendimiento, x="rendimiento", kde=True, ax=eje)
        eje.set(xlabel="Rendimiento", ylabel="Frecuencia")
        st.pyplot(figura, width="stretch")
        plt.close(figura)

    with col2:
        st.subheader("Diagrama de caja del rendimiento")
        figura, eje = plt.subplots(figsize=(7, 4))
        sns.boxplot(data=rendimiento, x="rendimiento", ax=eje)
        eje.set(xlabel="Rendimiento")
        st.pyplot(figura, width="stretch")
        plt.close(figura)

    st.subheader("Comparaciones de rendimiento")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Según tipo de suelo**")
        orden_suelo = sorted(rendimiento["suelo"].dropna().unique())
        figura, eje = plt.subplots(figsize=(7, 4))
        sns.boxplot(
            data=rendimiento,
            x="suelo",
            y="rendimiento",
            order=orden_suelo,
            ax=eje,
        )
        eje.set(xlabel="Tipo de suelo", ylabel="Rendimiento")
        st.pyplot(figura, width="stretch")
        plt.close(figura)
        resumen_suelo = (
            rendimiento.groupby("suelo")["rendimiento"]
            .agg(n="count", media="mean", mediana="median", desviacion="std")
            .round(2)
        )
        st.dataframe(resumen_suelo, width="stretch")

    with col2:
        st.markdown("**Según riego**")
        orden_riego = sorted(rendimiento["riego"].dropna().unique())
        figura, eje = plt.subplots(figsize=(7, 4))
        sns.boxplot(
            data=rendimiento,
            x="riego",
            y="rendimiento",
            order=orden_riego,
            ax=eje,
        )
        eje.set(xlabel="Riego", ylabel="Rendimiento")
        st.pyplot(figura, width="stretch")
        plt.close(figura)
        resumen_riego = (
            rendimiento.groupby("riego")["rendimiento"]
            .agg(n="count", media="mean", mediana="median", desviacion="std")
            .round(2)
        )
        st.dataframe(resumen_riego, width="stretch")
