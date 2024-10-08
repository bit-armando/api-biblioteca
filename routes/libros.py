from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from sql.databases.biblioteca import engine
from sql.databases.biblioteca import SessionLocal
from sql.schemas import biblioteca as schemas
from sql.models import biblioteca as models

router = APIRouter(
        prefix="/libros",
        tags=["libros"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/autor/')
def all_autors(db: Session = Depends(get_db)):
    return db.query(models.Autor).all()

@router.get('/autor/{id}')
def get_autor(id: int,
              db: Session = Depends(get_db)):
    return db.query(models.Autor).filter(models.Autor.id == id).first()
@router.post("/autor")
def add_author(autor: schemas.Autor,
               db: Session = Depends(get_db)):
    db_item = models.Autor(**autor.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.put('/autor/{id}')
def update_autor(autor: schemas.Autor,
                 id:int,
                 db: Session = Depends(get_db)):
    item = db.query(models.Autor).filter(models.Autor.id == id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Autor not found")

    item.nombre = autor.nombre
    item.apellido_p = autor.apellido_p
    item.apellido_m = autor.apellido_m

    db.commit()
    db.refresh(item)
    return item


@router.delete('/autor/{id}')
def delete_autor(id: int,
                 db: Session = Depends(get_db)):
    item = db.query(models.Autor).filter(models.Autor.id == id).first()

    if not item:
        raise HTTPException(status_code=404, detail="Autor not found")

    db.delete(item)
    db.commit()
    return {"message": "Autor deleted"}






@router.post("/editorial")
def add_editorial(item: schemas.Editorial,
               db: Session = Depends(get_db)):
    db_item = models.Editorial(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item