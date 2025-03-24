import cloudinary.uploader
import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables
load_dotenv()

# Cloudinary helpers
def upload_to_cloudinary(file):
    try:
        result = cloudinary.uploader.upload(file)
        return result.get("url")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cloudinary upload failed: {str(e)}")
