from pydantic import BaseModel
from typing import Optional
from datetime import date

# ConfiguracionCorreo schemas
class ConfiguracionCorreoBase(BaseModel):
    id_remitente: int
    estado: int
    proveedor: str
    servidor_smtp: str
    puerto: int
    usuarios_smtp: str
    clave_smtp: str
    usa_tls: int
    usa_ssl: int

class ConfiguracionCorreoCreate(ConfiguracionCorreoBase):
    pass

class ConfiguracionCorreoUpdate(BaseModel):
    estado: Optional[int] = None
    proveedor: Optional[str] = None
    servidor_smtp: Optional[str] = None
    puerto: Optional[int] = None
    usuarios_smtp: Optional[str] = None
    clave_smtp: Optional[str] = None
    usa_tls: Optional[int] = None
    usa_ssl: Optional[int] = None

class ConfiguracionCorreo(ConfiguracionCorreoBase):
    id: int
    fecha_creacion: Optional[date] = None
    fecha_modificacion: Optional[date] = None
    id_usuario_creacion: Optional[int] = None
    id_usuario_modificacion: Optional[int] = None

    class Config:
        from_attributes = True