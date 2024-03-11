from typing import List, Optional

from pydantic import BaseModel


class WeatherDescription(BaseModel):
    description: str
    code: int
    icon: str


class CommonWeatherParams(BaseModel):
    app_temp: Optional[float] = None
    aqi: Optional[int] = None
    city_name: Optional[str] = None
    clouds: int
    country_code: Optional[str] = None
    datetime: str
    dewpt: float
    dni: Optional[float] = None
    elev_angle: Optional[float] = None
    ghi: Optional[float] = None
    h_angle: Optional[float] = None
    lat: Optional[float] = None
    lon: Optional[float] = None
    ob_time: Optional[str] = None
    pod: Optional[str] = None
    precip: float
    pres: float
    rh: int
    slp: float
    snow: int
    solar_rad: Optional[float] = None
    sources: Optional[List[str]] = None
    state_code: Optional[str] = None
    station: Optional[str] = None
    sunrise: Optional[str] = None
    sunset: Optional[str] = None
    temp: float
    timezone: Optional[str] = None
    ts: int
    uv: float
    vis: float
    weather: WeatherDescription
    wind_cdir: str
    wind_cdir_full: str
    wind_dir: int
    wind_spd: float
    timestamp_utc: Optional[str] = None
    timestamp_local: Optional[str] = None


class WeatherData(CommonWeatherParams):
    gust: Optional[float] = None
    snow_depth: Optional[int] = None
    pop: Optional[int] = None
    ozone: Optional[float] = None
    clouds_hi: Optional[int] = None
    clouds_low: Optional[int] = None
    clouds_mid: Optional[int] = None


class WeatherForecastData(CommonWeatherParams):
    valid_date: str
    max_temp: float
    min_temp: float
    high_temp: float
    low_temp: float
    app_max_temp: float
    app_min_temp: float
    pop: Optional[int] = None
    precip: float
    snow: int
    snow_depth: Optional[int] = None
    pres: float
    slp: float
    dewpt: float
    rh: int
    wind_gust_spd: Optional[float] = None
    wind_spd: float
    wind_dir: int
    wind_cdir: str
    wind_cdir_full: str
    sunrise_ts: Optional[int] = None
    sunset_ts: Optional[int] = None
    moon_phase: Optional[float] = None
    moon_phase_lunation: Optional[float] = None
    moonrise_ts: Optional[int] = None
    moonset_ts: Optional[int] = None
    uv: Optional[float] = None
    max_dhi: Optional[float] = None
    ozone: Optional[float] = None
    clouds_hi: Optional[int] = None
    clouds_low: Optional[int] = None
    clouds_mid: Optional[int] = None


class WeatherForecast(BaseModel):
    lat: float
    lon: float
    timezone: str
    city_name: str
    country_code: str
    state_code: str
    data: List[WeatherForecastData]


class WeatherDataResponseModel(BaseModel):
    data: WeatherData


class WeatherForecastResponseModel(BaseModel):
    data: WeatherForecast | List[WeatherForecast]
