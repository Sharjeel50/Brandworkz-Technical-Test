import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)


class Settings:
    WEATHER_API_BASE_URL: str = "https://weatherbit-v1-mashape.p.rapidapi.com"
    HEADERS: dict = {
        "X-RapidAPI-Key": os.getenv("X_RAPID_API_KEY"),
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }


settings = Settings()
