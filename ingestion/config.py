import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
  postgres_host: str
  postgres_port: int
  postgres_db: str
  postgres_user: str
  postgres_password: str
  latitude: float
  longitude: float
  city_name: str
  start_date: str
  end_date: str

def get_settings() -> Settings:
  """
  Load project settings from environment variables.

  Returns:
    Settings: immutable settings object for the ingestion pipeline.

  Raises:
    ValueError: if required environment variables are missing or invalid.
  """
  try:
    return Settings(
      postgres_host=os.getenv("POSTGRES_HOST", "localhost"),
      postgres_port=int(os.getenv("POSTGRES_PORT", "5432")),
      postgres_db=_get_required_env("POSTGRES_DB"),
      postgres_user=_get_required_env("POSTGRES_USER"),
      postgres_password=_get_required_env("POSTGRES_PASSWORD"),
      latitude=float(_get_required_env("LATITUDE")),
      longitude=float(_get_required_env("LONGITUDE")),
      city_name=_get_required_env("CITY_NAME"),
      start_date=_get_required_env("START_DATE"),
      end_date=_get_required_env("END_DATE"),
    )
  except ValueError as exc:
    raise ValueError(f"Invalid environment configuration: {exc}") from exc

def _get_required_env(name: str) -> str:
  value = os.getenv(name)
  if value is None or value.strip() == "":
    raise ValueError(f"Missing required environment variable: {name}")
  return value.strip()