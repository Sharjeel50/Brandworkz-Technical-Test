import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import WeatherCard from "../components/WeatherCard";
import "./css/weather-page.css"; // Import your CSS file

function WeatherPage() {
  const WEATHER_API_URL = import.meta.env.VITE_WEATHER_API_URL;

  const navigate = useNavigate();

  const [selectedCountry, setSelectedCountry] = useState<string>("London");
  const [countryWeather, setCountryWeather] = useState<WeatherData | null>(
    null
  );

  const { isLoading, error, refetch } = useQuery({
    queryKey: ["current-weather", selectedCountry],
    enabled: false,
    queryFn: () =>
      fetch(
        `${WEATHER_API_URL}/current?country=${selectedCountry}&use_temporary_data=true`
      )
        .then((res) => res.json())
        .then((response_json) => {
          setCountryWeather(response_json.data);
          return response_json.data;
        }),
  });

  const handleCountryChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedCountry(event.target.value);
  };

  return (
    <div className="weather-page">
      <div className="page-title">WeatherPage</div>
      <div className="country-selector">
        <label>Select a country: </label>
        <select value={selectedCountry} onChange={handleCountryChange}>
          <option value="London">London</option>
          <option value="New York">New York</option>
          <option value="Mumbai">Mumbai</option>
          <option value="Sydney">Sydney</option>
          <option value="Tokyo">Tokyo</option>
        </select>
      </div>

      <button onClick={() => refetch()}>Get Weather</button>

      {countryWeather && (
        <WeatherCard
          weatherData={countryWeather}
          isLoading={isLoading}
          error={error}
        />
      )}
      <div className="forecast-button">
        <button
          onClick={() => {
            navigate("/forecast");
          }}
        >
          16 Day Forecast
        </button>
      </div>
    </div>
  );
}

export default WeatherPage;
