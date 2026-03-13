# FastAPI Project

This is a new FastAPI project.

## Installation

1. Install dependencies:
   pip install -r requirements.txt

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

## API Documentation

Visit http://127.0.0.1:8000/docs for interactive API docs.