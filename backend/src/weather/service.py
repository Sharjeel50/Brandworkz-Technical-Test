import aiohttp
from fastapi import HTTPException, status

from .constants import *
from .schemas import WeatherData, WeatherForecast
from src.config import settings


async def async_weather_request(request_client: aiohttp.ClientSession, url: str, params: dict,
                                return_initial: bool = False) -> WeatherData | WeatherForecast:
    weather_request = await request_client.get(url=url, params=params)

    if not weather_request.ok:
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail={"msg": "Failed to retrieve weather information."})

    weather_information = await weather_request.json()
    if return_initial:
        return weather_information["data"][0]
    return weather_information


async def get_current_weather(request_client: aiohttp.ClientSession, country: CountryEnum) -> WeatherData:
    current_weather_ep: str = f"{settings.WEATHER_API_BASE_URL}/current"
    return await async_weather_request(request_client, current_weather_ep, COUNTRY_LAT_LON.get(country.value),
                                       return_initial=True)


async def get_weather_forecast_16_days(request_client: aiohttp.ClientSession, country: CountryEnum) -> WeatherForecast:
    forecast_16th_day_ep: str = f"{settings.WEATHER_API_BASE_URL}/forecast/daily"
    return await async_weather_request(request_client, forecast_16th_day_ep, COUNTRY_LAT_LON.get(country.value))
