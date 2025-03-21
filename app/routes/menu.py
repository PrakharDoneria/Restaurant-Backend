from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import menu_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/menu")
def get_menu(db: Session = Depends(get_db)):
    return menu_service.get_all_menu_items(db)

@router.post("/menu")
def add_menu_item(item_data: dict, db: Session = Depends(get_db)):
    return menu_service.add_menu_item(db, item_data)

@router.put("/menu/{id}")
def update_menu_item(id: int, update_data: dict, db: Session = Depends(get_db)):
    return menu_service.update_menu_item(db, id, update_data)

@router.delete("/menu/{id}")
def delete_menu_item(id: int, db: Session = Depends(get_db)):
    return menu_service.delete_menu_item(db, id)
