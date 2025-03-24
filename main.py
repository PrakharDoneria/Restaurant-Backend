from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from admin import router as admin_router
from user import router as user_router
from upload import router as upload_router
import uvicorn

# Create the FastAPI app
app = FastAPI(
    title="Pizza Restaurant API",
    description="Backend API for managing a pizza restaurant, built with FastAPI and MongoDB",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

# Include the routers
app.include_router(admin_router, tags=["Admin"])
app.include_router(user_router, tags=["User"])
app.include_router(upload_router, tags=["Uploads"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Pizza Restaurant API!"}

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)