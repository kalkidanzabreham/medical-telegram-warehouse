# Medical Telegram Data Warehouse

## Overview
This project builds an end-to-end data platform to analyze Ethiopian medical and pharmaceutical businesses using public Telegram data.

## Architecture (Interim)
Telegram → Raw Data Lake (JSON) → PostgreSQL → dbt Transformations → Star Schema

## Task 1: Data Scraping & Data Lake
- Scraped public Telegram medical channels using Telethon
- Stored raw JSON files in a partitioned data lake
- Logged scraping activity and errors

### Data Lake Structure
data/raw/telegram_messages/YYYY-MM-DD/channel_name.json

## Task 2: Data Modeling & Transformation
- Loaded raw data into PostgreSQL `raw.telegram_messages`
- Used dbt for transformations
- Built a star schema:
  - `dim_channels`
  - `dim_dates`
  - `fct_messages`
- Implemented dbt tests for data quality
- Generated dbt documentation

## How to Run
```bash
docker-compose up -d
python src/scraper.py
python src/load_raw_to_postgres.py
dbt run
dbt test
```
