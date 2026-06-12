# 📘 Assignment: Statistics with Python

## 🎯 Objective

Practicar análisis estadístico básico en Python usando `pandas` y `numpy`: cálculo de medidas descriptivas, agregaciones, correlaciones y visualizaciones simples.

## 📝 Tasks

### 🛠️ Task 1 — Estadísticas descriptivas

#### Description
Cargar un CSV y calcular estadísticas básicas (media, mediana, desviación estándar, percentiles).

#### Requirements
Completed program should:

- Leer un archivo CSV con columnas numéricas.
- Calcular y mostrar: media, mediana, moda, desviación estándar, mínimo, máximo y percentiles (25, 50, 75).
- Usar `pandas`/`numpy` para los cálculos.

### 🛠️ Task 2 — Agrupaciones y agregaciones

#### Description
Agrupar datos por una columna categórica y calcular estadísticas por grupo.

#### Requirements
Completed program should:

- Agrupar por una columna (`group`) y calcular agregaciones (media, conteo, suma).
- Mostrar resultados ordenados por la media descendente.

### 🛠️ Task 3 — Correlación y limpieza básica

#### Description
Calcular correlaciones entre variables y manejar valores faltantes.

#### Requirements
Completed program should:

- Calcular la matriz de correlación entre columnas numéricas.
- Mostrar pares con correlación absoluta mayor a un umbral (por ejemplo, 0.5).
- Manejar valores faltantes: opción para eliminar filas con NA o rellenar con la media.

### 🛠️ Task 4 — CLI y pruebas (opcional)

#### Description
Proveer una interfaz de línea de comandos para ejecutar análisis y (opcional) pruebas con `pytest`.

#### Requirements
Completed program should:

- Incluir un script `analysis.py` que acepte argumentos: `--path`, `--group-by`, `--fill-na`.
- (Opcional) Incluir pruebas que verifiquen funciones clave.

## ⏱️ Estimated difficulty & time

Intermedio; 2–4 horas.

## ✅ Submission

- Subir `assignments/python-statistics/README.md`, `analysis.py`, `sample.csv` y `requirements.txt`.
- Registrar la asignación con `node .github/skills/new-assignment/scripts/update-config.js <id> "<title>" "<description>"` y añadir attachments con `add-attachment.js`.
