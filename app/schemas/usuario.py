from pydantic import BaseModel
from typing import Optional
from datetime import date

# Usuario schemas
class UsuarioBase(BaseModel):
    nombre: str
    email: str
    contraseña: str
    estado: int

class UsuarioCreate(UsuarioBase):
    nombre: str
    email: str
    contraseña: str
    estado: int

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    contraseña: Optional[str] = None
    estado: Optional[int] = None

class Usuario(UsuarioBase):
    id: int
    fecha_creacion: Optional[date] = None
    fecha_modificacion: Optional[date] = None
    id_usuario_creacion: Optional[int] = None
    id_usuario_modificacion: Optional[int] = None

    class Config:
        from_attributes = True
        exclude = {"contraseña"}  # Exclude password from response