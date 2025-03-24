# Pizza Restaurant API

Welcome to the Pizza Restaurant API! This backend is built with FastAPI, MongoDB, and Cloudinary to manage a pizza restaurant's operations, including handling pizzas, categories, orders, and image uploads.

## Table of Contents
1. [Getting Started](#getting-started)
2. [API Endpoints](#api-endpoints)
    - [Admin Endpoints](#admin-endpoints)
    - [User Endpoints](#user-endpoints)
    - [Image Upload Endpoint](#image-upload-endpoint)
3. [Sample Responses](#sample-responses)

---

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pizza-api.git
   cd pizza-api
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with the following environment variables:
   ```
   MONGO_URI=mongodb+srv://your-connection-string
   DB_NAME=pizzaDB
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Visit the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

---

## API Endpoints

### Admin Endpoints

#### 1. Add a New Category
- **Endpoint**: `POST /api/admin/category`
- **Body**:
  ```json
  {
    "name": "Vegetarian Pizzas",
    "description": "Pizzas with only vegetarian toppings"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Category added successfully",
    "category_id": "641c12345abc6789def01234"
  }
  ```

#### 2. Add a New Pizza
- **Endpoint**: `POST /api/admin/pizza`
- **Body**:
  ```json
  {
    "name": "Margherita",
    "category_id": "641c12345abc6789def01234",
    "price": 299,
    "image_url": "http://example.com/image.jpg"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Pizza added successfully",
    "pizza_id": "641c98765zyx5432wvu10987"
  }
  ```

#### 3. Update Order Status
- **Endpoint**: `PUT /api/admin/order/{order_id}`
- **Body**:
  ```json
  {
    "status": "Completed"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Order status updated successfully"
  }
  ```

#### 4. View All Orders
- **Endpoint**: `GET /api/admin/orders`
- **Response**:
  ```json
  {
    "orders": [
      {
        "order_id": "641f12345abc6789def01234",
        "user_info": {
          "name": "John Doe",
          "mobile": "9876543210",
          "address": "123 Pizza Street"
        },
        "pizzas": [
          {
            "pizzaId": "641c98765zyx5432wvu10987",
            "name": "Margherita",
            "quantity": 2,
            "price": 299
          }
        ],
        "total_price": 598,
        "status": "Pending",
        "is_free": false
      }
    ]
  }
  ```

---

### User Endpoints

#### 1. View Available Pizzas
- **Endpoint**: `GET /api/user/pizzas`
- **Response**:
  ```json
  {
    "pizzas": [
      {
        "pizza_id": "641c98765zyx5432wvu10987",
        "name": "Margherita",
        "category_id": "641c12345abc6789def01234",
        "price": 299,
        "image_url": "http://example.com/image.jpg"
      }
    ]
  }
  ```

#### 2. Place an Order
- **Endpoint**: `POST /api/user/order`
- **Body**:
  ```json
  {
    "name": "John Doe",
    "mobile": "9876543210",
    "address": "123 Pizza Street",
    "pizzas": [
      {
        "pizzaId": "641c98765zyx5432wvu10987",
        "quantity": 2
      }
    ]
  }
  ```
- **Response**:
  ```json
  {
    "message": "Order placed successfully",
    "order_id": "641f12345abc6789def01234"
  }
  ```

---

### Image Upload Endpoint

#### 1. Upload an Image
- **Endpoint**: `POST /api/upload`
- **Body**: File (binary)
- **Response**:
  ```json
  {
    "message": "Image uploaded successfully",
    "url": "http://res.cloudinary.com/your-cloud-name/image/upload/v1234567890/image.jpg"
  }
  ```

---

## Sample Responses

### Error Responses
1. **Category Not Found**:
   - **Status**: `404 Not Found`
   - **Response**:
     ```json
     {
       "detail": "Category not found"
     }
     ```

2. **Invalid Input**:
   - **Status**: `400 Bad Request`
   - **Response**:
     ```json
     {
       "detail": "At least one pizza must be ordered"
     }
     ```

3. **Order Not Found**:
   - **Status**: `404 Not Found`
   - **Response**:
     ```json
     {
       "detail": "Order not found or status update failed"
     }
     ```

---

Feel free to contribute or report any issues. Happy coding! 🚀
```
