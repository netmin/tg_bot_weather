import os

from pathlib import Path

BOT_TOKEN = os.getenv('BOT_TOKEN')
BASE_URL = 'https://example.com'  # Webhook domain
WEBHOOK_PATH = f'/tg/webhooks/bot/{BOT_TOKEN}'
WEBHOOK_URL = f'{BASE_URL}{WEBHOOK_PATH}'

LOGS_BASE_PATH = str(Path(__file__).parent.parent / 'logs')

admins = []
