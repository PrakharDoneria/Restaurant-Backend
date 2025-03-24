from fastapi import APIRouter, HTTPException
from models import Pizza, Order

router = APIRouter()

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

# Place an order
@router.post("/api/user/order")
def place_order(name: str, mobile: str, address: str, pizzas: list):
    if not pizzas or len(pizzas) == 0:
        raise HTTPException(status_code=400, detail="At least one pizza must be ordered")

    # Calculate total price
    total_price = 0
    pizza_details = []
    for pizza in pizzas:
        pizza_info = Pizza.get_by_id(pizza["pizzaId"])
        if not pizza_info:
            raise HTTPException(status_code=404, detail=f"Pizza with ID {pizza['pizzaId']} not found")
        
        pizza_info["_id"] = str(pizza_info["_id"])  # Convert ObjectId to string
        pizza_info["category_id"] = str(pizza_info["category_id"])  # Convert ObjectId to string
        
        pizza_details.append({
            "pizzaId": pizza_info["_id"],
            "quantity": pizza["quantity"],
            "price": pizza_info["price"],
            "name": pizza_info["name"]
        })
        total_price += pizza_info["price"] * pizza["quantity"]

    user_info = {
        "name": name,
        "mobile": mobile,
        "address": address
    }

    order = Order(
        user_info=user_info,
        pizzas=pizza_details,
        total_price=total_price
    )
    order_id = order.save()

    return {"message": "Order placed successfully", "order_id": str(order_id)}
