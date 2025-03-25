from fastapi import APIRouter, HTTPException
from models import Category, Pizza, Order
from bson import ObjectId

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

# View all orders (with ObjectId fix)
@router.get("/api/admin/orders")
def get_all_orders():
    try:
        orders = Order.get_all()
        
        # Convert ObjectId to string for serialization
        formatted_orders = []
        for order in orders:
            order["_id"] = str(order["_id"])  # Convert ObjectId to string
            if "pizzas" in order:  # Ensure pizzas list is properly formatted
                for pizza in order["pizzas"]:
                    if "pizza_id" in pizza:
                        pizza["pizza_id"] = str(pizza["pizza_id"])
            formatted_orders.append(order)

        return {"orders": formatted_orders}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch orders: {str(e)}")

# Get all category names and IDs
@router.get("/api/admin/categories")
def get_all_categories():
    try:
        categories = Category.get_all()
        category_list = [{"id": str(category["_id"]), "name": category["name"]} for category in categories]
        return {"categories": category_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch categories: {str(e)}")
