from typing import Iterable

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extras import execute_batch

from ingestion.config import Settings

UPSERT_WEATHER_SQL = """
INSERT INTO analytics.raw_weather_history (
  city_name,
  latitude,
  longitude,
  weather_date,
  temperature_2m_mean,
  temperature_2m_max,
  temperature_2m_min,
  precipitation_sum,
  ingestion_source
)
VALUES (
  %s, %s, %s, %s, %s, %s, %s, %s, %s
)
ON CONFLICT (city_name, weather_date)
DO UPDATE SET
  latitude = EXCLUDED.latitude,
  longitude = EXCLUDED.longitude,
  temperature_2m_mean = EXCLUDED.temperature_2m_mean,
  temperature_2m_max = EXCLUDED.temperature_2m_max,
  temperature_2m_min = EXCLUDED.temperature_2m_min,
  precipitation_sum = EXCLUDED.precipitation_sum,
  ingestion_source = EXCLUDED.ingestion_source,
  ingested_at = CURRENT_TIMESTAMP;
"""

def get_connection(settings: Settings) -> connection:
  """
  Create a PostgreSQL connection using project settings.
  """
  return psycopg2.connect(
    host=settings.postgres_host,
    port=settings.postgres_port,
    dbname=settings.postgres_db,
    user=settings.postgres_user,
    password=settings.postgres_password,
  )

def upsert_weather_rows(conn: connection, rows: Iterable[tuple]) -> int:
  """
  Insert or update weather rows in PostgreSQL.

  Args:
    conn: open PostgreSQL connection.
    rows: iterable of row tuples.

  Returns:
    int: number of input rows processed.
  """
  rows = list(rows)
  if not rows:
    return 0

  with conn.cursor() as cursor:
    execute_batch(cursor, UPSERT_WEATHER_SQL, rows, page_size=100)

  conn.commit()
  return len(rows)