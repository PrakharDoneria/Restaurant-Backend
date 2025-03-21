from sqlalchemy.orm import Session
from app.models.menu import Menu
from fastapi import HTTPException

def get_all_menu_items(db: Session):
    return db.query(Menu).all()

def add_menu_item(db: Session, item_data: dict):
    item = Menu(**item_data)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def update_menu_item(db: Session, item_id: int, update_data: dict):
    item = db.query(Menu).filter(Menu.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in update_data.items():
        setattr(item, key, value)
    
    db.commit()
    return item

def delete_menu_item(db: Session, item_id: int):
    item = db.query(Menu).filter(Menu.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}
