from bson import ObjectId
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection setup
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
categories_collection = db["categories"]
pizzas_collection = db["pizzas"]
orders_collection = db["orders"]

# Models
class Category:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description

    def save(self):
        category_data = {
            "name": self.name,
            "description": self.description
        }
        result = categories_collection.insert_one(category_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(categories_collection.find({}))

    @staticmethod
    def get_by_id(category_id):
        return categories_collection.find_one({"_id": ObjectId(category_id)})


class Pizza:
    def __init__(self, name, category_id, price, image_url=""):
        self.name = name
        self.category_id = ObjectId(category_id)
        self.price = price
        self.image_url = image_url

    def save(self):
        pizza_data = {
            "name": self.name,
            "category_id": self.category_id,
            "price": self.price,
            "image_url": self.image_url
        }
        result = pizzas_collection.insert_one(pizza_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(pizzas_collection.find({}))

    @staticmethod
    def get_by_id(pizza_id):
        return pizzas_collection.find_one({"_id": ObjectId(pizza_id)})


class Order:
    def __init__(self, user_info, pizzas, total_price, status="Pending", is_free=False):
        self.user_info = user_info
        self.pizzas = pizzas
        self.total_price = total_price
        self.status = status
        self.is_free = is_free

    def save(self):
        order_data = {
            "user_info": self.user_info,
            "pizzas": self.pizzas,
            "total_price": self.total_price,
            "status": self.status,
            "is_free": self.is_free
        }
        result = orders_collection.insert_one(order_data)
        return str(result.inserted_id)

    @staticmethod
    def get_all():
        return list(orders_collection.find({}))

    @staticmethod
    def get_by_id(order_id):
        return orders_collection.find_one({"_id": ObjectId(order_id)})

    @staticmethod
    def update_status(order_id, new_status):
        return orders_collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"status": new_status}}
        )

    @staticmethod
    def mark_as_free(order_id):
        return orders_collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"is_free": True}}
        )
