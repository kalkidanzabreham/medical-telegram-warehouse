import os
import json
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

cur = conn.cursor()

cur.execute("""
CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.telegram_messages (
    message_id BIGINT,
    channel_name TEXT,
    message_date TIMESTAMP,
    message_text TEXT,
    has_media BOOLEAN,
    views INT,
    forwards INT
);
""")

base_path = "data/raw/telegram_messages"

for date_folder in os.listdir(base_path):
    folder = os.path.join(base_path, date_folder)
    for file in os.listdir(folder):
        with open(os.path.join(folder, file)) as f:
            records = json.load(f)

        for r in records:
            cur.execute("""
            INSERT INTO raw.telegram_messages VALUES (%s,%s,%s,%s,%s,%s,%s)
            """, (
                r["message_id"],
                r["channel_name"],
                r["message_date"],
                r["message_text"],
                r["has_media"],
                r["views"],
                r["forwards"]
            ))

conn.commit()
cur.close()
conn.close()
