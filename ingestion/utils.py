from typing import Any

def build_weather_rows(
  payload: dict[str, Any],
  city_name: str,
  latitude: float,
  longitude: float,
) -> list[tuple]:
  """
  Transform API JSON payload into database-ready tuples.

  Args:
      payload: JSON payload returned by the weather API.
      city_name: logical city name used in the project.
      latitude: source latitude.
      longitude: source longitude.

  Returns:
      list[tuple]: rows ready for insertion into PostgreSQL.
  """
  daily = payload["daily"]

  dates = daily["time"]
  temp_mean = daily["temperature_2m_mean"]
  temp_max = daily["temperature_2m_max"]
  temp_min = daily["temperature_2m_min"]
  precipitation = daily["precipitation_sum"]

  row_count = len(dates)

  expected_lengths = [
    len(temp_mean),
    len(temp_max),
    len(temp_min),
    len(precipitation),
  ]

  if any(length != row_count for length in expected_lengths):
    raise ValueError("API daily arrays do not have consistent lengths.")

  rows = []
  for idx in range(row_count):
    rows.append(
      (
        city_name,
        latitude,
        longitude,
        dates[idx],
        temp_mean[idx],
        temp_max[idx],
        temp_min[idx],
        precipitation[idx],
        "open-meteo",
      )
    )

  return rows