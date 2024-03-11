interface WeatherDescription {
  description: string;
  code: number;
  icon: string;
}

interface CommonWeatherParams {
  app_temp?: number | null;
  aqi?: number | null;
  city_name?: string | null;
  clouds: number;
  country_code?: string | null;
  datetime: string;
  dewpt: number;
  dni?: number | null;
  elev_angle?: number | null;
  ghi?: number | null;
  h_angle?: number | null;
  lat?: number | null;
  lon?: number | null;
  ob_time?: string | null;
  pod?: string | null;
  precip: number;
  pres: number;
  rh: number;
  slp: number;
  snow: number;
  solar_rad?: number | null;
  sources?: string[] | null;
  state_code?: string | null;
  station?: string | null;
  sunrise?: string | null;
  sunset?: string | null;
  temp: number;
  timezone?: string | null;
  ts: number;
  uv?: number | null;
  vis: number;
  weather: WeatherDescription;
  wind_cdir: string;
  wind_cdir_full: string;
  wind_dir: number;
  wind_spd: number;
  timestamp_utc?: string | null;
  timestamp_local?: string | null;
}

interface WeatherData extends CommonWeatherParams {
  gust?: number | null;
  snow_depth?: number | null;
  pop?: number | null;
  ozone?: number | null;
  clouds_hi?: number | null;
  clouds_low?: number | null;
  clouds_mid?: number | null;
}

interface WeatherForecastData extends CommonWeatherParams {
  valid_date: string;
  max_temp: number;
  min_temp: number;
  high_temp: number;
  low_temp: number;
  app_max_temp: number;
  app_min_temp: number;
  pop?: number | null;
  precip: number;
  snow: number;
  snow_depth?: number | null;
  pres: number;
  slp: number;
  dewpt: number;
  rh: number;
  wind_gust_spd?: number | null;
  wind_spd: number;
  wind_dir: number;
  wind_cdir: string;
  wind_cdir_full: string;
  sunrise_ts?: number | null;
  sunset_ts?: number | null;
  moon_phase?: number | null;
  moon_phase_lunation?: number | null;
  moonrise_ts?: number | null;
  moonset_ts?: number | null;
  max_dhi?: number | null;
  ozone?: number | null;
  clouds_hi?: number | null;
  clouds_low?: number | null;
  clouds_mid?: number | null;
}

interface WeatherForecast {
  lat: number;
  lon: number;
  timezone: string;
  city_name: string;
  country_code: string;
  state_code: string;
  data: WeatherForecastData[];
}
