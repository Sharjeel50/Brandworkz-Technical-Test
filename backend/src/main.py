from contextlib import asynccontextmanager

import aiohttp
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import settings
from src.weather import router as weather_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.async_requests_client = aiohttp.ClientSession(headers=settings.HEADERS)
    yield
    await app.async_requests_client.close()


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_routes.router)
