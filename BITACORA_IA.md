
# Bitácora de uso de IA

**Asignatura:** Estadística Aplicada con Python y R  
**Programa:** Ingeniería Agrícola  
**Universidad:** Universidad de Sucre  
**Proyecto:** Análisis estadístico del cultivo de sorgo en Tolú  
**Herramienta:** GitHub Copilot (modo Agente)  
**Modelo mostrado en el chat:** Auto (Balance). El modelo específico no se muestra. 

## Prompt 1 – Entorno virtual, .gitignore y requirements.txt

### Prompt usado (texto exacto)

Actúa como tutor de Python y Streamlit para estudiantes de Ingeniería Agrícola.
Responde en español y explica en una o dos líneas cada paso antes de ejecutarlo.
Estamos en un GitHub Codespace (Linux) dentro de mi repositorio app-estadistica-agricola,
que por ahora solo tiene README.md. Prepara el proyecto así:
1. Crea un entorno virtual llamado .venv con: python -m venv .venv
2. Actívalo con: source .venv/bin/activate  y verifica con: which python
3. Configura VS Code para usar .venv/bin/python como intérprete (archivo .vscode/settings.json).
4. Crea un .gitignore para Python que excluya: .venv/, __pycache__/, *.pyc,
   .ipynb_checkpoints/, .streamlit/secrets.toml y .DS_Store
5. Crea requirements.txt con: streamlit, pandas, numpy, scipy, matplotlib, seaborn, statsmodels
6. Instala las dependencias con: .venv/bin/pip install -r requirements.txt
7. Verifica la instalación imprimiendo la versión de cada librería.
No crees ningún otro archivo y no hagas commits. Al final muéstrame el árbol de archivos
(sin .venv) y explícame en 5 líneas para qué sirven el entorno virtual, .gitignore y requirements.txt.

### Comandos que aprobé

Durante la configuración se preparó el entorno virtual `.venv` y se utilizaron sus herramientas de Python.

Los comandos solicitados fueron:

- `python -m venv .venv`
- `source .venv/bin/activate`
- `which python`
- `.venv/bin/pip install -r requirements.txt`

También se crearon `.gitignore`, `requirements.txt` y `.vscode/settings.json`.

La aprobación individual de cada comando debe confirmarse en el historial de Copilot.

### Comandos o cambios que rechacé o corregí, y por qué

Durante la configuración, GitHub Copilot detectó que el archivo `.gitignore` ya existía en el repositorio, por lo que indicó que debía revisarlo antes de modificarlo para evitar sobrescribir información.

Copilot ejecutó el comando `ls -la` y en el historial aparece una acción de lectura de `.gitignore`.

También se registró una llamada a herramienta denegada. Sin embargo, no fue posible identificar con certeza cuál fue la acción rechazada ni su motivo.

## Prompt 2 – App de Streamlit

### Prompt usado (texto exacto)

Actúa como tutor de Python y Streamlit para Ingeniería Agrícola de la Universidad de Sucre.

Trabaja en mi repositorio app-estadistica-agricola.

Ya tengo configurado el entorno virtual .venv y las dependencias instaladas. También tengo los archivos datos/parcelas.csv, datos/clima_mensual.csv, datos/muestra10.csv y datos/metadatos.json.

Necesito crear una aplicación con Streamlit en un archivo llamado app.py.

La aplicación debe incluir:

1. Inicio: presentación del proyecto, cultivo de sorgo, municipio de Tolú y número de parcelas (87).
2. Datos: lectura de los archivos CSV, visualización de tablas y estadísticas descriptivas.
3. Análisis Exploratorio de Datos (EDA): gráficos del rendimiento, histograma, diagrama de caja y comparaciones según tipo de suelo y riego.

Utiliza pandas, numpy, matplotlib y seaborn cuando sea necesario.

Revisa primero la estructura real de los archivos para utilizar correctamente sus columnas.

Explica brevemente cada paso antes de ejecutarlo. No modifiques generar_datos.py ni los archivos de datos. No hagas commits todavía.

Al terminar, explícame cómo ejecutar la aplicación desde la terminal de Codespaces.

### ¿Funcionó al primer intento?

Durante el desarrollo se detectaron errores de sintaxis en Python, relacionados con el uso de palabras como `importar` y `como`, que no corresponden a las instrucciones válidas del lenguaje.

Se corrigieron por `import` y `as`, respectivamente.

Posteriormente, la aplicación pudo ejecutarse mediante Streamlit y mostrar las secciones Inicio, Datos y EDA.

### ¿Coincidió la muestra de 10 parcelas con mi cálculo a mano?

Sí. La verificación realizada manualmente y mediante Python y R produjo resultados coincidentes, considerando el redondeo.

- Media: 4.701 t/ha.
- Mediana: 4.205 t/ha.
- Varianza muestral: 2.9760 (t/ha)².
- Desviación estándar: 1.7251 t/ha.
- Coeficiente de variación: 36.70 %.
- Parcelas atípicas: P020 y P035.

## Prompt 3 – Actualización del repositorio

### Prompt usado (texto exacto)

Actúa como mi asistente de control de versiones con Git. Explica cada comando antes de
ejecutarlo y espera mi aprobación.
1. Ejecuta git status y confirma que .venv/ NO aparece; si aparece, corrige .gitignore
   antes de continuar.
2. Ejecuta git pull para traer los cambios que haya en GitHub.
3. Agrupa los archivos pendientes en commits separados y lógicos (por ejemplo: src/ y
   app.py; pages/; evidencias/; otros). Cada mensaje en español debe empezar por "[agente]"
   y describir el cambio.
4. Ejecuta git push y muéstrame git log --oneline -20.
5. Explícame en 3 líneas la diferencia entre hacer commit y hacer push, y dame la URL de mi
   repositorio en GitHub.

### Commits que creó el agente

No se identificaron commits con el prefijo [agente]
en el historial revisado.

Los cambios del proyecto se guardaron mediante
commits manuales y desde la interfaz web de GitHub.

Aunque utilicé GitHub Copilot para apoyar el
desarrollo, no se comprobó que el agente realizara
commits directamente.

Los siguientes commits fueron realizados manualmente y no deben atribuirse al agente:

- `29accdc`: Agrega aplicación Streamlit agrícola.
- `a54433a`: Completa verificaciones en Python y R.
- `27511d7`: Completa hallazgos del EDA en README.

Estos cambios se subieron correctamente a la rama `main` del repositorio.

**Repositorio:** https://github.com/jisoto22/app-estadistica-agricola

## Reflexión

Aprendí a configurar un entorno virtual de Python y organizar los archivos de un proyecto.
Comprendí cómo ejecutar una aplicación de Streamlit desde GitHub Codespaces.
Aprendí a comprobar los cálculos estadísticos utilizando Python y R.
Observé que la inteligencia artificial puede generar errores de sintaxis que deben revisarse.
También comprendí la importancia de verificar los resultados manualmente antes de aceptarlos.
Aprendí a utilizar los comandos de Git para guardar y subir mis cambios al repositorio.

**¿Detuve el Codespace al terminar cada sesión?:** Si
