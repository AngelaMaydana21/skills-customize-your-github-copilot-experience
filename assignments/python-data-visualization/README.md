# 📘 Assignment: Python Data Visualization

## 🎯 Objective

Aprender a visualizar datos en Python usando `matplotlib` y opcionalmente `plotly`. Los estudiantes crearán gráficos básicos (líneas, barras, histogramas), añadirán etiquetas y leyendas, y guardarán las figuras.

## 📝 Tasks

### 🛠️ Task 1 — Gráficos básicos

#### Description
Cargar un conjunto de datos simple y crear gráficos básicos: gráfico de líneas y de barras.

#### Requirements
Completed program should:

- Leer un archivo CSV con columnas numéricas.
- Dibujar un gráfico de líneas y un gráfico de barras con `matplotlib`.
- Añadir título, etiquetas de ejes y leyenda.
- Guardar los gráficos como imagen (`.png`).

### 🛠️ Task 2 — Estilizado y exportación

#### Description
Mejorar la presentación del gráfico y exportar en diferentes formatos.

#### Requirements
Completed program should:

- Cambiar colores, estilos de línea y tamaños de figura.
- Guardar al menos una figura en PNG y otra en SVG.
- (Opcional) Crear una versión interactiva usando `plotly`.

### 🛠️ Task 3 — Exploración y análisis

#### Description
Aplicar transformaciones sencillas y visualizar resultados (por ejemplo, agregación por categoría o ventana móvil).

#### Requirements
Completed program should:

- Agrupar o agregar datos según una columna y graficar el resultado.
- (Opcional) Calcular una media móvil y graficarla sobre la serie original.

## ⏱️ Estimated difficulty & time

Intermedio; 1.5–3 horas.

## ✅ Submission

- Subir `assignments/python-data-visualization/README.md`, `visualize.py`, `sample.csv` y `requirements.txt`.
- Registrar la asignación con el script `update-config.js` y añadir attachments con `add-attachment.js`.

## Local testing

Instalar dependencias y ejecutar ejemplos:

```bash
python -m pip install -r assignments/python-data-visualization/requirements.txt
python assignments/python-data-visualization/visualize.py sample.csv --line month value --out-dir output
```
