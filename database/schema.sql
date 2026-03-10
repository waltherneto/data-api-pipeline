CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.raw_weather_history (
    weather_id BIGSERIAL PRIMARY KEY,
    city_name VARCHAR(100) NOT NULL,
    latitude NUMERIC(8, 4) NOT NULL,
    longitude NUMERIC(8, 4) NOT NULL,
    weather_date DATE NOT NULL,
    temperature_2m_mean NUMERIC(5, 2),
    temperature_2m_max NUMERIC(5, 2),
    temperature_2m_min NUMERIC(5, 2),
    precipitation_sum NUMERIC(6, 2),
    ingestion_source VARCHAR(100) NOT NULL DEFAULT 'open-meteo',
    ingested_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_raw_weather_city_date UNIQUE (city_name, weather_date)
);