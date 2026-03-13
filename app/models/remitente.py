from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

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