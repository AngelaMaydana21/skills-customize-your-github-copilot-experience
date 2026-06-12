# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprende a diseñar y construir una API REST con FastAPI, creando rutas CRUD, validando datos con Pydantic y usando documentación automática.

## 📝 Tasks

### 🛠️ Task 1 — Scaffold the API

#### Description
Crea una aplicación FastAPI con endpoints para gestionar una colección simple de recursos (`items`).

#### Requirements
Completed program should:

- Exponer endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}` y `DELETE /items/{id}`.
- Usar modelos Pydantic para validar la entrada y la salida.
- Mantener los datos en memoria usando una lista o diccionario.
- Incluir documentación automática accesible en `/docs`.

### 🛠️ Task 2 — Validación y manejo de errores

#### Description
Agrega validación de datos y manejo de respuestas de error claras.

#### Requirements
Completed program should:

- Validar campos requeridos y tipos con Pydantic.
- Devolver códigos HTTP adecuados: `201` para creación, `400` para solicitudes inválidas y `404` para recursos no encontrados.
- Manejar IDs no existentes con una respuesta `404`.

### 🛠️ Task 3 — Extensiones opcionales

#### Description
Mejoras adicionales para quienes terminan rápido.

#### Requirements
Completed program may:

- Añadir búsqueda o filtrado en `GET /items`.
- Guardar y cargar datos en un archivo JSON simple.
- Incluir pruebas básicas con `pytest`.

## ⏱️ Estimated difficulty & time

Intermedio; de 2 a 4 horas según las mejoras que se agreguen.

## ✅ Submission

- Asegúrate de que `assignments/fastapi-rest-apis/README.md`, `main.py` y `requirements.txt` estén presentes.
- Ejecuta el servidor de FastAPI con Uvicorn y comprueba las rutas.
