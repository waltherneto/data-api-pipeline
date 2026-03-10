from ingestion.api_client import fetch_weather_data
from ingestion.config import get_settings
from ingestion.db import get_connection, upsert_weather_rows
from ingestion.utils import build_weather_rows

def main() -> None:
  settings = get_settings()

  print("Starting weather ingestion pipeline...")
  print(
    f"City: {settings.city_name} | "
    f"Coordinates: ({settings.latitude}, {settings.longitude}) | "
    f"Period: {settings.start_date} to {settings.end_date}"
  )

  payload = fetch_weather_data(
    latitude=settings.latitude,
    longitude=settings.longitude,
    start_date=settings.start_date,
    end_date=settings.end_date,
  )

  rows = build_weather_rows(
    payload=payload,
    city_name=settings.city_name,
    latitude=settings.latitude,
    longitude=settings.longitude,
  )

  conn = get_connection(settings)
  try:
    processed_rows = upsert_weather_rows(conn, rows)
  finally:
    conn.close()

  print("Weather ingestion completed successfully.")
  print(f"Rows processed: {processed_rows}")

if __name__ == "__main__":
  main()