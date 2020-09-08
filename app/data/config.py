import os
import json

from pathlib import Path

BOT_TOKEN = os.getenv('BOT_API_TOKEN')
BASE_URL = 'https://example.com'  # Webhook domain
WEBHOOK_PATH = f'/tg/webhooks/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')

admins = [
    487136793,
]

base_url = 'http://api.openweathermap.org/data/2.5/onecall?'
app_id = os.getenv('APP_ID')

