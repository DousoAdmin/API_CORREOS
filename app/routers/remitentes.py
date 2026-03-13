from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.remitente import Remitente
from ..schemas.remitente import Remitente as RemitenteSchema, RemitenteCreate, RemitenteUpdate

router = APIRouter(prefix="/remitentes", tags=["remitentes"])

@router.get("/", response_model=list[RemitenteSchema])
def read_remitentes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    remitentes = db.query(Remitente).offset(skip).limit(limit).all()
    return remitentes

@router.get("/{remitente_id}", response_model=RemitenteSchema)
def read_remitente(remitente_id: int, db: Session = Depends(get_db)):
    db_remitente = db.query(Remitente).filter(Remitente.id == remitente_id).first()
    if db_remitente is None:
        raise HTTPException(status_code=404, detail="Remitente not found")
    return db_remitente

@router.post("/", response_model=RemitenteSchema)
def create_remitente(remitente: RemitenteCreate, db: Session = Depends(get_db)):
    db_remitente = Remitente(**remitente.dict())
    db.add(db_remitente)
    db.commit()
    db.refresh(db_remitente)
    return db_remitente

@router.put("/{remitente_id}", response_model=RemitenteSchema)
def update_remitente(remitente_id: int, remitente_update: RemitenteUpdate, db: Session = Depends(get_db)):
    db_remitente = db.query(Remitente).filter(Remitente.id == remitente_id).first()
    if db_remitente is None:
        raise HTTPException(status_code=404, detail="Remitente not found")
    for key, value in remitente_update.dict(exclude_unset=True).items():
        setattr(db_remitente, key, value)
    db.commit()
    db.refresh(db_remitente)
    return db_remitente

@router.delete("/{remitente_id}")
def delete_remitente(remitente_id: int, db: Session = Depends(get_db)):
    db_remitente = db.query(Remitente).filter(Remitente.id == remitente_id).first()
    if db_remitente is None:
        raise HTTPException(status_code=404, detail="Remitente not found")
    db.delete(db_remitente)
    db.commit()
    return {"message": "Remitente deleted"}