import asyncio
from typing import Optional

from fastapi import APIRouter, Request, status

from . import service
from .constants import (
    CountryEnum,
    WeatherDataExampleResponse,
    WeatherForecastAllCountries
)
from .schemas import WeatherDataResponseModel, WeatherForecastResponseModel

router = APIRouter(prefix='/weather')


@router.get(
    "/current",
    summary="Get Current Weather",
    description="Retrieve the current weather information for specific cities, including London, New York, "
                "Mumbai, Sydney, and Tokyo.",
    response_model=WeatherDataResponseModel,
    responses={
        status.HTTP_200_OK: {
            "description": "Successful Response",
            "content": {
                "application/json": {
                    "example": {"data": WeatherDataExampleResponse}
                }
            },
        }
    }
)
async def get_current_weather(
    request: Request, country: CountryEnum, use_temporary_data: bool = False
):
    """
    Get the current weather details for the specified city.

    Parameters:
      - country: The country for which weather information is requested. Choose from London, New York, Mumbai, Sydney, Tokyo.
      - temporary_data: If API limits have been reached, temporary data can be returned by setting this to true when calling this endpoint.

    Returns:
      - WeatherDataResponseModel: The current weather data for the specified city.

    Example:
      Calling `/current?country=London` will return the current weather for London.
    """
    if use_temporary_data:
        return WeatherDataResponseModel(data=WeatherDataExampleResponse)

    weather_data = await service.get_current_weather(
        request.app.async_requests_client, country
    )
    return WeatherDataResponseModel(data=weather_data)


@router.get(
    "/forecast",
    summary="Get 16-Day Weather Forecast",
    description="Retrieve the 16-day weather forecast for specific cities, including London, New York, "
                "Mumbai, Sydney, and Tokyo.",
    response_model=WeatherForecastResponseModel
)
async def get_weather_forecast_16_days(
    request: Request, country: Optional[CountryEnum] = None, use_temporary_data: bool = False
):
    """
    Get the 16-day weather forecast for the specified country.

    Parameters:
      - country: The country for which the 16-day weather forecast is requested. Choose from London, New York, Mumbai, Sydney, Tokyo.
                 Optionally, passing no country will return forecasts for all countries mentioned above.
      - temporary_data: If API limits have been reached, temporary data can be returned by setting this to true when calling this endpoint.

    Returns:
      - WeatherForecastResponseModel: The 16-day weather forecast data for the specified city.

    Example:
      Calling `/forecast?country=London` will return the 16-day weather forecast for London.
    """
    if use_temporary_data:
        return WeatherForecastResponseModel(data=WeatherForecastAllCountries)

    async_requests_client = request.app.async_requests_client

    if country:
        weather_forecast = await service.get_weather_forecast_16_days(
            async_requests_client, country
        )
        return WeatherForecastResponseModel(data=weather_forecast)

    forecast_coroutines = [
        asyncio.create_task(service.get_weather_forecast_16_days(async_requests_client, i))
        for i in CountryEnum
    ]
    country_forecasts = await asyncio.gather(*forecast_coroutines)

    return WeatherForecastResponseModel(data=country_forecasts)
