# Data API Pipeline

A portfolio project that demonstrates how to ingest data from an external API, store the data in PostgreSQL, and prepare it for analytics using SQL.

## Project Overview

This project simulates a small but realistic data engineering workflow for a company that wants to analyze external weather data for business planning and trend monitoring.

The pipeline collects historical weather data from a public API, loads it into a PostgreSQL database, and prepares the dataset for downstream analytical queries.

## Business Scenario

A company wants to monitor external data such as weather conditions to support operational and analytical decisions.

In this project, the selected external source is historical weather data. The pipeline stores daily metrics such as average temperature, maximum temperature, minimum temperature, and precipitation for a selected city and date range.

## What This Project Demonstrates

* API-based data ingestion using Python
* Environment-based configuration using `.env`
* PostgreSQL schema design for raw data storage
* Idempotent loading with `INSERT ... ON CONFLICT`
* Clear repository structure for reproducibility
* SQL-ready data preparation for analytics

## Tech Stack

* Python 3.12.x
* Requests
* PostgreSQL
* SQL
* psycopg2-binary
* python-dotenv

## Data Source

This project uses the Open-Meteo historical weather API as the external data source.

## Pipeline Flow

```text
Open-Meteo API
    ↓
Python ingestion script
    ↓
PostgreSQL raw storage
    ↓
Analytical SQL queries
```

## Repository Structure

```text
data-api-pipeline/
│
├── ingestion/
│   ├── config.py
│   ├── api_client.py
│   ├── db.py
│   ├── load_weather_data.py
│   └── utils.py
│
├── database/
│   └── schema.sql
│
├── analysis/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Environment Setup

This project was developed using **Python 3.12.x**.

### 1) Create virtual environment

```bash
python -m venv .venv
```

### 2) Activate virtual environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bat
.venv\Scripts\activate.bat
```

### 3) Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Configuration

Create a local `.env` file based on `.env.example`.

Example:

```env
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=data_api_pipeline
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

LATITUDE=-23.5505
LONGITUDE=-46.6333
CITY_NAME=Sao Paulo
START_DATE=2025-01-01
END_DATE=2025-01-10
```

## Database Setup

Create the PostgreSQL database first:

```sql
CREATE DATABASE data_api_pipeline;
```

Then apply the schema:

```bash
psql -U postgres -d data_api_pipeline -f database/schema.sql
```

## Database Design

The project currently uses a raw ingestion table:

* `analytics.raw_weather_history`

### Table Granularity

One row per:

* city
* weather date

### Stored Metrics

* `temperature_2m_mean`
* `temperature_2m_max`
* `temperature_2m_min`
* `precipitation_sum`

### Important Design Choices

* A dedicated `analytics` schema keeps the project organized
* A unique constraint on `(city_name, weather_date)` prevents duplicate daily records
* `ingested_at` supports ingestion auditability
* `ingestion_source` captures source traceability

## Running the Ingestion Pipeline

After the database schema is created and the `.env` file is configured, run:

```bash
python -m ingestion.load_weather_data
```

## What the Ingestion Pipeline Does

The ingestion pipeline:

1. loads environment variables
2. calls the Open-Meteo historical weather API
3. validates the API response structure
4. transforms daily arrays into row-based records
5. inserts or updates rows in PostgreSQL using upsert logic
6. prints a summary of processed rows

## Idempotent Load Behavior

The pipeline uses PostgreSQL `INSERT ... ON CONFLICT` logic to support safe reprocessing.

That means you can rerun the same date range for the same city without creating duplicate records.

## Example Validation Query

```sql
SELECT
    city_name,
    weather_date,
    temperature_2m_mean,
    temperature_2m_max,
    temperature_2m_min,
    precipitation_sum,
    ingested_at
FROM analytics.raw_weather_history
ORDER BY weather_date;
```

## Current Project Status

The project currently includes:

* repository bootstrap
* PostgreSQL raw schema
* Python ingestion pipeline
* environment configuration

The next step is to add the analytics layer with SQL views and analytical queries.

## Future Improvements

Possible future extensions for this project include:

* multi-city ingestion
* scheduling with cron or orchestration tools
* partitioning strategies for larger datasets
* analytical views for monthly and seasonal trends
* dashboard integration with BI tools

## License

This project is intended for portfolio and educational purposes.
