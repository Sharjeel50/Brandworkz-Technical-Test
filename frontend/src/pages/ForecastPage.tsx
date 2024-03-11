import React, { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import ForecastCards from "../components/ForecastCards";
import "./css/forecast-page.css"; // Import your CSS file for additional styling
import { useNavigate } from "react-router-dom";

function ForecastPage() {
  const WEATHER_API_URL = import.meta.env.VITE_WEATHER_API_URL;
  const USE_TEMP_DATA = import.meta.env.VITE_TEMP_DATA;

  const navigate = useNavigate();

  const { isLoading, data } = useQuery({
    queryKey: ["all-country-forecasts"],
    queryFn: () =>
      fetch(`${WEATHER_API_URL}/forecast?use_temporary_data=${USE_TEMP_DATA}`)
        .then((res) => res.json())
        .then((response_json) => response_json.data),
  });

  const [minTemp, setMinTemp] = useState<number | undefined>(undefined);
  const [maxTemp, setMaxTemp] = useState<number | undefined>(undefined);

  const handleMinTempChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setMinTemp(e.target.value !== "" ? parseFloat(e.target.value) : undefined);

  const handleMaxTempChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setMaxTemp(e.target.value !== "" ? parseFloat(e.target.value) : undefined);

  if (isLoading) return "Fetching forecasts..";

  const filteredForecasts = data.map((countryForecast: WeatherForecast) => ({
    ...countryForecast,
    data: countryForecast.data.filter((day) => {
      const meetsMinTemp = minTemp === undefined || day.min_temp >= minTemp;
      const meetsMaxTemp = maxTemp === undefined || day.max_temp <= maxTemp;
      return meetsMinTemp && meetsMaxTemp;
    }),
  }));

  return (
    <div className="forecast-page">
      <div>
        <button onClick={() => navigate("/")}>Get current weather</button>
        <h3>Forecasts</h3>
      </div>
      <div className="filter-section">
        <div className="filter-item">
          <label htmlFor="minTemp">Min Temperature: </label>
          <input
            type="number"
            id="minTemp"
            value={minTemp}
            onChange={handleMinTempChange}
          />
        </div>
        <div className="filter-item">
          <label htmlFor="maxTemp">Max Temperature: </label>
          <input
            type="number"
            id="maxTemp"
            value={maxTemp}
            onChange={handleMaxTempChange}
          />
        </div>
      </div>
      <div className="forecast-cards-container">
        {filteredForecasts.map((countryForecast: WeatherForecast) => (
          <ForecastCards
            key={countryForecast.city_name}
            weatherForecast={countryForecast}
          />
        ))}
      </div>
    </div>
  );
}

export default ForecastPage;
