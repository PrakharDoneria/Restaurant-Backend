from fastapi import APIRouter, File, UploadFile, HTTPException
import cloudinary.uploader
import os
from dotenv import load_dotenv

router = APIRouter()

# Load environment variables
load_dotenv()

# Cloudinary configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# Upload an image
@router.post("/api/upload")
def upload_image(file: UploadFile = File(...)):
    try:
        # Upload file to Cloudinary
        result = cloudinary.uploader.upload(file.file)
        return {"message": "Image uploaded successfully", "url": result.get("url")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {str(e)}")
