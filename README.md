# FastAPI Project

This is a new FastAPI project with database integration for managing users, senders, and email configurations.

## Installation

1. Install dependencies:
   pip install -r requirements.txt

## Database Setup

1. Create a MySQL database named `mydb`.
2. Update the `SQLALCHEMY_DATABASE_URL` in `app/database.py` with your MySQL credentials.
3. Run the SQL script in `scripts/base de datos.sql` to create tables.

## Running the Application

Run the server with:
uvicorn app.main:app --reload

Visit http://127.0.0.1:8000/ for the hello world endpoint.

## Running with Docker

1. Build the Docker image:
   docker build -t fastapi-app .

2. Run the container:
   docker run -p 8000:80 fastapi-app

Or use Docker Compose:
   docker-compose up --build

Visit http://127.0.0.1:8000/ for the hello world endpoint.

## API Endpoints

- **Usuarios**: `/usuarios` - CRUD for users
- **Remitentes**: `/remitentes` - CRUD for senders
- **Configuraciones**: `/configuraciones` - CRUD for email configurations

## API Documentation

Visit http://127.0.0.1:8000/docs for interactive API docs.