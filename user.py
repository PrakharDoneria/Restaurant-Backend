from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from models import Pizza, Order

router = APIRouter()

# Define Pydantic models for request validation
class PizzaOrderItem(BaseModel):
    pizzaId: str
    quantity: int

class OrderRequest(BaseModel):
    name: str
    mobile: str
    address: str
    pizzas: List[PizzaOrderItem]

# View available pizzas
@router.get("/api/user/pizzas")
def get_pizzas():
    pizzas = Pizza.get_all()
    if not pizzas:
        raise HTTPException(status_code=404, detail="No pizzas found")
    
    # Convert ObjectId to string for each pizza
    for pizza in pizzas:
        pizza["_id"] = str(pizza["_id"])
        pizza["category_id"] = str(pizza["category_id"])
    
    return {"pizzas": pizzas}

# Get order status
@router.get("/api/user/status")
def get_order_status(id: str):
    order = Order.get_by_id(id)
    
    if order:
        return {
            "order_id": id,
            "current_status": order["status"]
        }
    
    raise HTTPException(status_code=404, detail="Order not found")

# Place an order
@router.post("/api/user/order")
def place_order(order: OrderRequest):
    if not order.pizzas or len(order.pizzas) == 0:
        raise HTTPException(status_code=400, detail="At least one pizza must be ordered")

    # Calculate total price
    total_price = 0
    pizza_details = []
    for pizza in order.pizzas:
        pizza_info = Pizza.get_by_id(pizza.pizzaId)
        if not pizza_info:
            raise HTTPException(status_code=404, detail=f"Pizza with ID {pizza.pizzaId} not found")
        
        pizza_info["_id"] = str(pizza_info["_id"])  # Convert ObjectId to string
        pizza_info["category_id"] = str(pizza_info["category_id"])  # Convert ObjectId to string
        
        pizza_details.append({
            "pizzaId": pizza_info["_id"],
            "quantity": pizza.quantity,
            "price": pizza_info["price"],
            "name": pizza_info["name"]
        })
        total_price += pizza_info["price"] * pizza.quantity

    user_info = {
        "name": order.name,
        "mobile": order.mobile,
        "address": order.address
    }

    order_instance = Order(
        user_info=user_info,
        pizzas=pizza_details,
        total_price=total_price
    )
    order_id = order_instance.save()

    return {"message": "Order placed successfully", "order_id": str(order_id)}
