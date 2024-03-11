import "./css/forecast-card.css";

interface Props {
  weatherForecast: WeatherForecast;
}

function ForecastCards({ weatherForecast }: Props) {
  return (
    <div className="forecast-container">
      <h5 className="city-name">{weatherForecast.city_name}</h5>
      {weatherForecast.data.length === 0 ? (
        <p>No matching temps!</p>
      ) : (
        <div className="cards-container">
          {weatherForecast.data.map((day) => (
            <div key={day.valid_date} className="forecast-card">
              <h6 className="date">{day.valid_date}</h6>
              <p className="temperature">Min Temp: {day.min_temp}&deg;C</p>
              <p className="temperature">Max Temp: {day.max_temp}&deg;C</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default ForecastCards;
