CREATE OR REPLACE VIEW analytics.vw_weather_monthly_summary AS
SELECT
    city_name,
    DATE_TRUNC('month', weather_date)::date AS month_start_date,
    COUNT(*) AS recorded_days,
    ROUND(AVG(temperature_2m_mean), 2) AS avg_temperature_mean,
    ROUND(AVG(temperature_2m_max), 2) AS avg_temperature_max,
    ROUND(AVG(temperature_2m_min), 2) AS avg_temperature_min,
    ROUND(SUM(precipitation_sum), 2) AS total_precipitation,
    ROUND(MAX(temperature_2m_max), 2) AS hottest_day_temperature,
    ROUND(MIN(temperature_2m_min), 2) AS coldest_day_temperature
FROM analytics.raw_weather_history
GROUP BY
    city_name,
    DATE_TRUNC('month', weather_date)::date;