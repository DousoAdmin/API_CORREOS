from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    email = Column(String(200))
    contraseña = Column(String(255))
    fecha_creacion = Column(Date)
    fecha_modificacion = Column(Date)
    id_usuario_creacion = Column(Integer)
    id_usuario_modificacion = Column(Integer)
    estado = Column(Integer)

    # Relationship
    remitentes = relationship("Remitente", back_populates="usuario")

class Remitente(Base):
    __tablename__ = "remitentes"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    nombre_remitente = Column(String(255))
    correo_remitente = Column(String(200))
    remitentescol = Column(String(45))  # Assuming telefono or similar
    estado = Column(Integer)
    fecha_creacion = Column(Date)
    fecha_modificacion = Column(Date)
    id_usuario_creacion = Column(Integer)
    id_usuario_modifica = Column(Integer)  # Assuming modificacion

    # Relationships
    usuario = relationship("Usuario", back_populates="remitentes")
    configuraciones = relationship("ConfiguracionCorreo", back_populates="remitente")

class ConfiguracionCorreo(Base):
    __tablename__ = "configuracion_correos"

    id = Column(Integer, primary_key=True, index=True)
    id_remitente = Column(Integer, ForeignKey("remitentes.id"))
    estado = Column(Integer)
    proveedor = Column(String(100))
    servidor_smtp = Column(String(150))
    puerto = Column(Integer)
    usuarios_smtp = Column(String(150))
    clave_smtp = Column(String(255))
    usa_tls = Column(Integer)
    usa_ssl = Column(Integer)
    fecha_creacion = Column(Date)
    fecha_modificacion = Column(Date)
    id_usuario_creacion = Column(Integer)
    id_usuario_modificacion = Column(Integer)

    # Relationship
    remitente = relationship("Remitente", back_populates="configuraciones")