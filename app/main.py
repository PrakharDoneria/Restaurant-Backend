from fastapi import FastAPI
from app.database import init_db
from app.routes import menu, order

# Create FastAPI app instance
app = FastAPI(title="Pizza Ordering API", description="API for managing pizza orders", version="1.0")

# Initialize database (create tables if they don’t exist)
init_db()

# Include API routes
app.include_router(menu.router, prefix="/api", tags=["Menu"])
app.include_router(order.router, prefix="/api", tags=["Orders"])

# Root endpoint
@app.get("/")
def home():
    return {"message": "Pizza API is running. Visit /docs for API documentation."}
