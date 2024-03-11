import React from "react";

interface WeatherCardProps {
  weatherData: WeatherData;
  isLoading: boolean;
  error: Error | null;
}

function WeatherCard({ weatherData, isLoading, error }: WeatherCardProps) {
  return (
    <div className="card-style">
      {isLoading ? (
        <h3>Fetching Weather Data..</h3>
      ) : (
        <div>
          <h3>{weatherData.city_name}</h3>
          <p>Temperature: {weatherData.temp}&deg;C</p>
          <p>
            Wind: {weatherData.wind_spd} m/s, {weatherData.wind_dir}&deg;
          </p>
          <p>Humidity: {weatherData.rh}%</p>
        </div>
      )}
    </div>
  );
}

export default WeatherCard;
