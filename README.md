Descripción del Proyecto:
Aplicación web para gestionar recetas, desarrollada con React en el frontend, FastAPI en el backend y PostgreSQL como base de datos. Permite a los usuarios registrar y gestionar sus propias recetas con un sistema de autenticación seguro.

Características:

Registro e inicio de sesión de usuarios.
Creación, edición y eliminación de recetas.
Filtrado de recetas por ingredientes y etiquetas.
Tecnologías Utilizadas:

Frontend: React, Axios, React Router.
Backend: FastAPI, SQLAlchemy, Uvicorn.
Base de Datos: PostgreSQL.
Contenedores: Docker y Docker Compose.
Despliegue: Render.
Requisitos Previos:
Asegúrate de tener instalados Python 3.10+, Node.js y npm, PostgreSQL, Docker y Docker Compose (opcional), y Git.

Instalación:

Clonar el repositorio:

git clone https://github.com/tu-usuario/recipe-app.git
cd recipe-app
Configurar el Frontend:

Navegar al directorio frontend y ejecutar npm install.
Configurar el Backend:

Navegar al directorio backend.
Crear un entorno virtual con python3 -m venv env y activarlo:
En Linux/Mac: source env/bin/activate
En Windows: .\env\Scripts\activate
Instalar las dependencias con pip install -r requirements.txt.
Variables de Entorno:

Crear un archivo .env tanto en frontend como en backend.

En frontend/.env:

REACT_APP_API_URL=http://localhost:8000
En backend/.env:

DATABASE_URL=postgresql://user:password@localhost:5432/recipes_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
Cómo Ejecutar el Proyecto:

Iniciar el Backend (FastAPI):

Navegar al directorio backend y ejecutar uvicorn main:app --reload.
El backend estará disponible en http://localhost:8000.
Iniciar el Frontend (React):

Navegar al directorio frontend y ejecutar npm start.
El frontend estará disponible en http://localhost:3000.
Uso de Docker:

Para construir y ejecutar los contenedores, asegúrate de estar en el directorio raíz del proyecto y ejecuta:

docker-compose up --build
Esto iniciará tanto el backend (FastAPI) como la base de datos PostgreSQL. El frontend estará en http://localhost:3000 y el backend en http://localhost:8000.
Para detener los contenedores, ejecuta:

docker-compose down
Despliegue en Render:

Conectar el repositorio de GitHub a Render.
Crear un nuevo servicio con la opción docker-compose.
Configurar las variables de entorno en Render.