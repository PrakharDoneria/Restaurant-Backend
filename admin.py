from fastapi import APIRouter, HTTPException
from models import Category, Pizza, Order

router = APIRouter()

# Add a new category
@router.post("/api/admin/category")
def add_category(name: str, description: str = ""):
    category = Category(name=name, description=description)
    category_id = category.save()
    if category_id:
        return {"message": "Category added successfully", "category_id": category_id}
    raise HTTPException(status_code=500, detail="Failed to add category")

# Add a new pizza
@router.post("/api/admin/pizza")
def add_pizza(name: str, category_id: str, price: float, image_url: str = ""):
    pizza = Pizza(name=name, category_id=category_id, price=price, image_url=image_url)
    pizza_id = pizza.save()
    if pizza_id:
        return {"message": "Pizza added successfully", "pizza_id": pizza_id}
    raise HTTPException(status_code=500, detail="Failed to add pizza")

# Update order status
@router.put("/api/admin/order/{order_id}")
def update_order_status(order_id: str, status: str):
    result = Order.update_status(order_id, status)
    if result.modified_count > 0:
        return {"message": "Order status updated successfully"}
    raise HTTPException(status_code=404, detail="Order not found or status update failed")

# View all orders
@router.get("/api/admin/orders")
def get_all_orders():
    orders = Order.get_all()
    return {"orders": orders}
