from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from ..database import Base

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