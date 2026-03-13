from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

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