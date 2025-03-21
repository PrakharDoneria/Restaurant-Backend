from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.order import Order

def place_order(db: Session, order_data: dict):
    order = Order(**order_data)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_orders_by_mobile(db: Session, mobile: str):
    return db.query(Order).filter(Order.mobile == mobile).all()

def get_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def update_order_status(db: Session, order_id: int, status: str):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = status
    db.commit()
    return {"message": "Order status updated"}

def cancel_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status.lower() != "pending":
        raise HTTPException(status_code=400, detail="Order cannot be cancelled")

    db.delete(order)
    db.commit()
    return {"message": "Order cancelled successfully"}
