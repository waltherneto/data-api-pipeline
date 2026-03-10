-- 1. Monthly weather trend summary
SELECT
    city_name,
    month_start_date,
    recorded_days,
    avg_temperature_mean,
    avg_temperature_max,
    avg_temperature_min,
    total_precipitation,
    hottest_day_temperature,
    coldest_day_temperature
FROM analytics.vw_weather_monthly_summary
ORDER BY city_name, month_start_date;


-- 2. Top 10 hottest days
SELECT
    city_name,
    weather_date,
    temperature_2m_max,
    temperature_2m_mean,
    temperature_2m_min,
    precipitation_sum
FROM analytics.raw_weather_history
ORDER BY temperature_2m_max DESC, weather_date ASC
LIMIT 10;


-- 3. Top 10 coldest days
SELECT
    city_name,
    weather_date,
    temperature_2m_min,
    temperature_2m_mean,
    temperature_2m_max,
    precipitation_sum
FROM analytics.raw_weather_history
ORDER BY temperature_2m_min ASC, weather_date ASC
LIMIT 10;


-- 4. Top 10 rainiest days
SELECT
    city_name,
    weather_date,
    precipitation_sum,
    temperature_2m_mean,
    temperature_2m_max,
    temperature_2m_min
FROM analytics.raw_weather_history
ORDER BY precipitation_sum DESC, weather_date ASC
LIMIT 10;


-- 5. Monthly precipitation totals
SELECT
    city_name,
    month_start_date,
    total_precipitation
FROM analytics.vw_weather_monthly_summary
ORDER BY city_name, month_start_date;


-- 6. Daily temperature range analysis
SELECT
    city_name,
    weather_date,
    temperature_2m_max,
    temperature_2m_min,
    ROUND((temperature_2m_max - temperature_2m_min), 2) AS daily_temperature_range
FROM analytics.raw_weather_history
ORDER BY daily_temperature_range DESC, weather_date ASC
LIMIT 10;