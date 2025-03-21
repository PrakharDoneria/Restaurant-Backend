# 🍕 Restaurant Backend API

This is a FastAPI-based backend for a pizza ordering system. The API allows users to view the menu, place orders, and retrieve order details.

## 🚀 Setup & Run

### 1️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 2️⃣ Start the Server
```sh
uvicorn app.main:app --reload
```

### 3️⃣ API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📂 API Endpoints & Sample Requests

### 1️⃣ Get Menu Items
**Endpoint:** `GET /api/menu`
#### 🔹 Sample Response
```json
[
    {"id": 1, "name": "Margherita", "price": 8.99},
    {"id": 2, "name": "Pepperoni", "price": 10.99}
]
```

---
### 2️⃣ Add a Menu Item
**Endpoint:** `POST /api/menu`
**Request Body:**
```json
{
    "name": "BBQ Chicken",
    "price": 12.99
}
```
#### 🔹 Sample Response
```json
{
    "id": 3,
    "name": "BBQ Chicken",
    "price": 12.99
}
```

---
### 3️⃣ Place an Order
**Endpoint:** `POST /api/order`
**Request Body:**
```json
{
    "customer_name": "John Doe",
    "mobile": "1234567890",
    "items": [
        {"pizza_id": 1, "quantity": 2},
        {"pizza_id": 2, "quantity": 1}
    ],
    "total_price": 28.97
}
```
#### 🔹 Sample Response
```json
{
    "id": 101,
    "customer_name": "John Doe",
    "mobile": "1234567890",
    "status": "Pending"
}
```

---
### 4️⃣ Get Orders by Mobile Number
**Endpoint:** `GET /api/orders?number=1234567890`
#### 🔹 Sample Response
```json
[
    {"id": 101, "customer_name": "John Doe", "mobile": "1234567890", "status": "Pending"}
]
```

---
### 5️⃣ Update Order Status
**Endpoint:** `PUT /api/order/{id}`
**Request Body:**
```json
{
    "status": "Completed"
}
```
#### 🔹 Sample Response
```json
{
    "message": "Order status updated"
}
```

---
### 6️⃣ Cancel an Order
**Endpoint:** `POST /api/order/cancel/{id}`
#### 🔹 Sample Response
```json
{
    "message": "Order cancelled successfully"
}
```

## 🛠️ Technologies Used
- **FastAPI** (Python Web Framework)
- **MySQL** (Database)
- **SQLAlchemy** (ORM for database operations)
- **Uvicorn** (ASGI Server)

## 🎯 Future Improvements
- Add payment integration
- Implement WebSockets for real-time order updates

🚀 **Enjoy your pizza! 🍕**