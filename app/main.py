from fastapi import FastAPI
from .database import engine, Base
from .routers import usuarios, remitentes, configuraciones, auth

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(usuarios.router)
app.include_router(remitentes.router)
app.include_router(configuraciones.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}