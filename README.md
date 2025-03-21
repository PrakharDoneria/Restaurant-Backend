# Pizza Restaurant API - README

## Overview
This is the backend API for a pizza restaurant, built using FastAPI and MySQL. It allows users to view the menu, place orders, and fetch orders using a mobile number. The admin panel can be used to add new menu items.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: MySQL
- **ORM**: SQLAlchemy

---

1. API documentation is available at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### 1. Get Menu Items
**Endpoint:** `GET /api/menu`

**Description:** Retrieves all menu items.

**Response:**
```json
[
    {
        "id": 1,
        "name": "Margherita",
        "price": 9.99,
        "category": "Vegetarian",
        "description": "Classic Margherita pizza with fresh basil",
        "image_url": "http://example.com/margherita.jpg"
    }
]
```

---

### 2. Add Menu Item (Admin Only)
**Endpoint:** `POST /api/menu`

**Description:** Adds a new menu item.

**Request Body:**
```json
{
    "name": "BBQ Chicken",
    "price": 12.99,
    "category": "Non-Vegetarian",
    "description": "BBQ Chicken pizza with onions and cheese",
    "image_url": "http://example.com/bbqchicken.jpg"
}
```

**Response:**
```json
{
    "message": "Menu item added successfully!",
    "item_id": 2
}
```

**Error Handling:**
- If `category` is missing, returns:
```json
{
    "detail": "Category cannot be null"
}
```

---

### 3. Place an Order
**Endpoint:** `POST /api/orders`

**Description:** Places a new order.

**Request Body:**
```json
{
    "customer_name": "John Doe",
    "mobile": "9876543210",
    "items": [
        {"pizza_id": 1, "quantity": 2},
        {"pizza_id": 2, "quantity": 1}
    ]
}
```

**Response:**
```json
{
    "order_id": 5,
    "message": "Order placed successfully!"
}
```

---

### 4. Get Orders by Mobile Number
**Endpoint:** `GET /api/orders?number=9876543210`

**Description:** Fetches all orders associated with a given mobile number.

**Response:**
```json
[
    {
        "order_id": 5,
        "customer_name": "John Doe",
        "mobile": "9876543210",
        "items": [
            {"pizza_name": "Margherita", "quantity": 2},
            {"pizza_name": "BBQ Chicken", "quantity": 1}
        ],
        "total_price": 32.97,
        "status": "Preparing"
    }
]
```

---

## Database Schema
### Menu Table
| Column      | Type         | Constraints  |
|------------|-------------|-------------|
| id         | INT         | PRIMARY KEY |
| name       | VARCHAR(100) | NOT NULL    |
| price      | DECIMAL(10,2) | NOT NULL    |
| category   | VARCHAR(50)  | NOT NULL    |
| description | TEXT        | NULLABLE    |
| image_url  | TEXT        | NULLABLE    |

### Orders Table
| Column        | Type         | Constraints  |
|--------------|-------------|-------------|
| id           | INT         | PRIMARY KEY |
| customer_name | VARCHAR(100) | NOT NULL   |
| mobile       | VARCHAR(15)  | NOT NULL   |
| total_price  | DECIMAL(10,2) | NOT NULL   |
| status       | VARCHAR(50)  | DEFAULT 'Preparing' |

---

## Notes
- The API does **not** require authentication.
- Orders can contain multiple pizzas.
- Menu items cannot be added without a category.
- Orders are fetched using `?number=` query parameter.

---

## Future Enhancements
- Implement authentication for the admin panel.
- Add payment gateway integration.
- Improve order tracking and status updates.