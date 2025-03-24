### **1. Add Category**
#### **Request**
```http
POST /api/admin/category?name=Vegetarian&description=Delicious veggie pizzas
```
#### **Response (200 OK)**
```json
{
  "message": "Category added successfully",
  "category": {
    "id": "12345",
    "name": "Vegetarian",
    "description": "Delicious veggie pizzas"
  }
}
```
#### **Response (422 Validation Error)**
```json
{
  "detail": [
    {
      "loc": ["query", "name"],
      "msg": "Field required",
      "type": "value_error.missing"
    }
  ]
}
```

---

### **2. Add Pizza**
#### **Request**
```http
POST /api/admin/pizza?name=Margherita&category_id=12345&price=12.99&image_url=https://example.com/margherita.jpg
```
#### **Response (200 OK)**
```json
{
  "message": "Pizza added successfully",
  "pizza": {
    "id": "67890",
    "name": "Margherita",
    "category_id": "12345",
    "price": 12.99,
    "image_url": "https://example.com/margherita.jpg"
  }
}
```

---

### **3. Update Order Status**
#### **Request**
```http
PUT /api/admin/order/98765?status=Delivered
```
#### **Response (200 OK)**
```json
{
  "message": "Order status updated successfully",
  "order": {
    "order_id": "98765",
    "status": "Delivered"
  }
}
```

---

### **4. Get All Orders**
#### **Request**
```http
GET /api/admin/orders
```
#### **Response (200 OK)**
```json
{
  "orders": [
    {
      "order_id": "98765",
      "name": "John Doe",
      "status": "Pending",
      "total_price": 25.99
    },
    {
      "order_id": "87654",
      "name": "Jane Doe",
      "status": "Delivered",
      "total_price": 18.50
    }
  ]
}
```

---

### **5. Get All Categories**
#### **Request**
```http
GET /api/admin/categories
```
#### **Response (200 OK)**
```json
{
  "categories": [
    {
      "id": "12345",
      "name": "Vegetarian",
      "description": "Delicious veggie pizzas"
    },
    {
      "id": "67890",
      "name": "Non-Vegetarian",
      "description": "Pizzas with meat toppings"
    }
  ]
}
```

---

### **6. Get Pizzas**
#### **Request**
```http
GET /api/user/pizzas
```
#### **Response (200 OK)**
```json
{
  "pizzas": [
    {
      "id": "67890",
      "name": "Margherita",
      "category": "Vegetarian",
      "price": 12.99,
      "image_url": "https://example.com/margherita.jpg"
    },
    {
      "id": "54321",
      "name": "Pepperoni",
      "category": "Non-Vegetarian",
      "price": 14.99,
      "image_url": "https://example.com/pepperoni.jpg"
    }
  ]
}
```

---

### **7. Place Order**
#### **Request**
```http
POST /api/user/order?name=John Doe&mobile=1234567890&address=123 Street, NY
Content-Type: multipart/form-data
```
#### **Request Body**
```json
{
  "pizzas": [
    {
      "pizza_id": "67890",
      "quantity": 2
    },
    {
      "pizza_id": "54321",
      "quantity": 1
    }
  ]
}
```
#### **Response (200 OK)**
```json
{
  "message": "Order placed successfully",
  "order_id": "98765",
  "total_price": 40.97
}
```

---

### **8. Upload Image**
#### **Request**
```http
POST /api/upload
Content-Type: multipart/form-data
```
#### **Request Body**
```json
{
  "file": "<binary file data>"
}
```
#### **Response (200 OK)**
```json
{
  "message": "Image uploaded successfully",
  "image_url": "https://example.com/uploads/image123.jpg"
}
```