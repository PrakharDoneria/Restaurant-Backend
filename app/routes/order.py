from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import order_service

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/order")
def place_order(order_data: dict, db: Session = Depends(get_db)):
    return order_service.place_order(db, order_data)

@router.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return order_service.get_all_orders(db)

@router.get("/orders/")
def get_orders_by_number(number: str, db: Session = Depends(get_db)):
    return order_service.get_orders_by_mobile(db, number)

@router.get("/order/{id}")
def get_order(id: int, db: Session = Depends(get_db)):
    return order_service.get_order_by_id(db, id)

@router.put("/order/{id}")
def update_order_status(id: int, status: str, db: Session = Depends(get_db)):
    return order_service.update_order_status(db, id, status)

@router.post("/order/cancel/{id}")
def cancel_order(id: int, db: Session = Depends(get_db)):
    return order_service.cancel_order(db, id)
