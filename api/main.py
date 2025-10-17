from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import random

app = FastAPI(title="Mock NASA API", version="1.0")

@app.get("/planetary/apod")
def get_apod(api_key: str = None):
    """
    Mock endpoint to simulate NASA's Astronomy Picture of the Day API.
    It ignores the API key and returns sample data.
    """
    # Random mock data for variety
    sample_titles = [
        "The Milky Way over the Desert",
        "Aurora over the Arctic Circle",
        "Eclipse Shadow on Earth",
        "Mars Rover Selfie",
        "Galactic Core Panorama"
    ]

    mock_data = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "explanation": "This is a mock response simulating NASA's APOD API.",
        "hdurl": "https://example.com/mock_hd_image.jpg",
        "media_type": "image",
        "service_version": "v1",
        "title": random.choice(sample_titles),
        "url": "https://example.com/mock_image.jpg"
    }

    return JSONResponse(content=mock_data)
