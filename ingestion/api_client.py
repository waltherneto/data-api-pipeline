from typing import Any
import requests

OPEN_METEO_ARCHIVE_URL = "https://archive-api.open-meteo.com/v1/archive"

def fetch_weather_data(
  latitude: float,
  longitude: float,
  start_date: str,
  end_date: str,
) -> dict[str, Any]:
  """
  Fetch daily historical weather data from Open-Meteo.

  Args:
    latitude: geographic latitude.
    longitude: geographic longitude.
    start_date: start date in YYYY-MM-DD format.
    end_date: end date in YYYY-MM-DD format.

  Returns:
    dict[str, Any]: parsed JSON response.

  Raises:
    requests.HTTPError: when the API returns an unsuccessful status code.
    ValueError: when the API response structure is incomplete.
  """
  params = {
    "latitude": latitude,
    "longitude": longitude,
    "start_date": start_date,
    "end_date": end_date,
    "daily": ",".join(
      [
        "temperature_2m_mean",
        "temperature_2m_max",
        "temperature_2m_min",
        "precipitation_sum",
      ]
    ),
    "timezone": "auto",
  }

  response = requests.get(
      OPEN_METEO_ARCHIVE_URL,
      params=params,
      timeout=30,
  )
  response.raise_for_status()

  payload = response.json()
  _validate_api_payload(payload)

  return payload

def _validate_api_payload(payload: dict[str, Any]) -> None:
  """
  Validate the minimum expected structure of the Open-Meteo response.
  """
  if "daily" not in payload:
    raise ValueError("API response does not contain 'daily' data.")

  required_daily_fields = [
    "time",
    "temperature_2m_mean",
    "temperature_2m_max",
    "temperature_2m_min",
    "precipitation_sum",
  ]

  missing_fields = [
    field for field in required_daily_fields if field not in payload["daily"]
  ]
  if missing_fields:
    raise ValueError(
      f"API response is missing expected daily fields: {missing_fields}"
    )