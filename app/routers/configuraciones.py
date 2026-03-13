from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.configuracion_correo import ConfiguracionCorreo
from ..schemas.configuracion_correo import ConfiguracionCorreo as ConfiguracionCorreoSchema, ConfiguracionCorreoCreate, ConfiguracionCorreoUpdate

router = APIRouter(prefix="/configuraciones", tags=["configuraciones"])

@router.get("/", response_model=list[ConfiguracionCorreoSchema])
def read_configuraciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    configuraciones = db.query(ConfiguracionCorreo).offset(skip).limit(limit).all()
    return configuraciones

@router.get("/{configuracion_id}", response_model=ConfiguracionCorreoSchema)
def read_configuracion(configuracion_id: int, db: Session = Depends(get_db)):
    db_configuracion = db.query(ConfiguracionCorreo).filter(ConfiguracionCorreo.id == configuracion_id).first()
    if db_configuracion is None:
        raise HTTPException(status_code=404, detail="Configuracion not found")
    return db_configuracion

@router.post("/", response_model=ConfiguracionCorreoSchema)
def create_configuracion(configuracion: ConfiguracionCorreoCreate, db: Session = Depends(get_db)):
    db_configuracion = ConfiguracionCorreo(**configuracion.dict())
    db.add(db_configuracion)
    db.commit()
    db.refresh(db_configuracion)
    return db_configuracion

@router.put("/{configuracion_id}", response_model=ConfiguracionCorreoSchema)
def update_configuracion(configuracion_id: int, configuracion_update: ConfiguracionCorreoUpdate, db: Session = Depends(get_db)):
    db_configuracion = db.query(ConfiguracionCorreo).filter(ConfiguracionCorreo.id == configuracion_id).first()
    if db_configuracion is None:
        raise HTTPException(status_code=404, detail="Configuracion not found")
    for key, value in configuracion_update.dict(exclude_unset=True).items():
        setattr(db_configuracion, key, value)
    db.commit()
    db.refresh(db_configuracion)
    return db_configuracion

@router.delete("/{configuracion_id}")
def delete_configuracion(configuracion_id: int, db: Session = Depends(get_db)):
    db_configuracion = db.query(ConfiguracionCorreo).filter(ConfiguracionCorreo.id == configuracion_id).first()
    if db_configuracion is None:
        raise HTTPException(status_code=404, detail="Configuracion not found")
    db.delete(db_configuracion)
    db.commit()
    return {"message": "Configuracion deleted"}