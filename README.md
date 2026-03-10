# Data API Pipeline

A small portfolio project that demonstrates how to ingest data from an external API, store it in PostgreSQL, and prepare it for analytics.

## Business Scenario

A company wants to monitor external weather data for a selected location and analyze historical trends such as temperature and precipitation.

## Tech Stack

* Python
* Requests
* PostgreSQL
* SQL

## Pipeline Flow

API
↓
Python ingestion script
↓
Database storage
↓
Analytical queries

## Repository Structure

```text
data-api-pipeline/
│
├── ingestion/
├── database/
├── analysis/
└── README.md
```

## Environment Setup

This project was developed using **Python 3.12.x**.

### Create virtual environment

```bash
python -m venv .venv
```

### Activate virtual environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bat
.venv\Scripts\activate.bat
```

### Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Project Status

This repository is being developed step by step as a portfolio project.
