from pydantic import BaseModel
from typing import Optional
from datetime import date

# Remitente schemas
class RemitenteBase(BaseModel):
    id_usuario: int
    nombre_remitente: str
    correo_remitente: str
    remitentescol: Optional[str] = None
    estado: int

class RemitenteCreate(RemitenteBase):
    pass

class RemitenteUpdate(BaseModel):
    nombre_remitente: Optional[str] = None
    correo_remitente: Optional[str] = None
    remitentescol: Optional[str] = None
    estado: Optional[int] = None

class Remitente(RemitenteBase):
    id: int
    fecha_creacion: Optional[date] = None
    fecha_modificacion: Optional[date] = None
    id_usuario_creacion: Optional[int] = None
    id_usuario_modifica: Optional[int] = None

    class Config:
        from_attributes = True