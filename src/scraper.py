import os
import json
import logging
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

CHANNELS = {
    "chemed": "https://t.me/chemed",
    "lobelia4cosmetics": "https://t.me/lobelia4cosmetics",
    "tikvahpharma": "https://t.me/tikvahpharma"
}

RAW_PATH = "data/raw/telegram_messages"
LOG_PATH = "logs/scraper.log"

os.makedirs("logs", exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO)

async def scrape_channel(client, name, url):
    today = datetime.today().strftime("%Y-%m-%d")
    save_dir = f"{RAW_PATH}/{today}"
    os.makedirs(save_dir, exist_ok=True)

    entity = await client.get_entity(url)
    messages = []

    async for message in client.iter_messages(entity, limit=500):
        messages.append({
            "message_id": message.id,
            "channel_name": name,
            "message_date": message.date.isoformat() if message.date else None,
            "message_text": message.text,
            "has_media": message.media is not None,
            "views": message.views,
            "forwards": message.forwards
        })

    with open(f"{save_dir}/{name}.json", "w") as f:
        json.dump(messages, f, indent=2)

    logging.info(f"Scraped {len(messages)} messages from {name}")

async def main():
    async with TelegramClient("session", API_ID, API_HASH) as client:
        for name, url in CHANNELS.items():
            try:
                await scrape_channel(client, name, url)
            except Exception as e:
                logging.error(f"Error scraping {name}: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
