# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practicar el procesamiento de texto en Python: manipulación de strings, lectura/escritura de archivos y transformaciones comunes (conteo, búsqueda, reemplazo).

## 📝 Tasks

### 🛠️ Task 1 — File I/O básico

#### Description
Escribe funciones para leer un archivo de texto, contar líneas y palabras, y devolver estadísticas básicas.

#### Requirements
Completed program should:

- Leer un archivo de texto y devolver el número de líneas, palabras y caracteres.
- Implementar una función `read_file(path)` que devuelva el contenido.
- Manejar errores si el archivo no existe (devolver un mensaje claro o lanzar excepción apropiada).

### 🛠️ Task 2 — Manipulación de strings

#### Description
Implementa funciones para buscar, reemplazar y normalizar texto.

#### Requirements
Completed program should:

- Implementar `find_occurrences(text, substring)` que devuelva las posiciones o el conteo de ocurrencias.
- Implementar `replace_text(text, old, new)` que reemplace todas las apariciones.
- Normalizar texto: convertir a minúsculas, eliminar puntuación básica y dividir en tokens.

### 🛠️ Task 3 — Uso práctico y pruebas

#### Description
Construir una pequeña CLI o funciones que a partir de un archivo ejecuten las tareas anteriores.

#### Requirements
Completed program should:

- Exponer funciones CLI básicas (por ejemplo, `--stats`, `--find`, `--replace`).
- Escribir resultados a un nuevo archivo si se solicita.
- (Opcional) Incluir pruebas con `pytest` que validen funciones clave.

## ⏱️ Estimated difficulty & time

Principiante-Intermedio; 1.5–3 horas.

## ✅ Submission

- Subir `assignments/python-text-processing/README.md`, `text_processor.py`, `sample.txt` y `requirements.txt`.
- Registrar la asignación usando el script `update-config.js` y registrar attachments con `add-attachment.js`.
