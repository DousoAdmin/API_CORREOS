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
    pass

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