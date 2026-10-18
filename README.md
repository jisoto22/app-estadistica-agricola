# App de Estadística Aplicada con Python y R — Ingeniería Agrícola (Unisucre)

**Estudiante:** José Ignacio Soto Viloria

**Código estudiantil:** 1104417335

**Grupo:** 2

**Cultivo asignado:** Sorgo

**Municipio:** Tolú

**Número de parcelas:** 87

**Huella digital:** D24A1388

**Docente:** Justo Fuentes

**Semestre:** 2026-2

## Descripción

Aplicación de Streamlit para realizar análisis estadísticos de parcelas agrícolas. El proyecto utiliza datos personalizados del cultivo de sorgo en Tolú.

La aplicación incluirá las páginas Inicio, Datos y Análisis Exploratorio de Datos (EDA). Las páginas de Regresión y Series de tiempo se desarrollarán posteriormente.

## Cómo ejecutar la aplicación

1. Abrir el repositorio en GitHub Codespaces.
2. Preparar el entorno virtual e instalar las bibliotecas:

   `python -m venv .venv`

   `.venv/bin/pip install -r requirements.txt`

3. Ejecutar la aplicación:

   `.venv/bin/streamlit run app.py`

## Hallazgos del EDA

- Se analizaron 87 parcelas agrícolas del cultivo de sorgo en el municipio de Tolú.
- Se identificaron 42 parcelas con suelo arcilloso, 31 con suelo franco y 14 con suelo arenoso.
- El suelo franco presentó el mayor rendimiento promedio, con 4,69 t/ha.
- Las parcelas con suelo arcilloso registraron un rendimiento promedio de 4,21 t/ha.
- El suelo arenoso presentó un rendimiento promedio de 4,20 t/ha.
- Las 37 parcelas con riego obtuvieron un rendimiento promedio de 4,49 t/ha.
- Las 50 parcelas sin riego presentaron un rendimiento promedio de 4,29 t/ha.
- Las parcelas con riego presentaron un rendimiento promedio 0,20 t/ha superior al de las parcelas sin riego, aunque esta diferencia no demuestra una relación causal.