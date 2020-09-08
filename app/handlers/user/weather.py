import json

import aiohttp
from aiogram import types
from data.config import base_url, app_id
from loader import dp
from utils.misc import rate_limit


@rate_limit(600)
@dp.message_handler(regexp='\w')
async def get_weather(message: types.Message):
    async with aiohttp.ClientSession() as session:
        with open('data/city.list.json', 'r') as f:
            data = json.load(f)
            for city in data:
                if city['name'] == 'Yekaterinburg':
                    lon = city['coord']['lon']
                    lat = city['coord']['lat']
        resp = await fetch(session, f'{base_url}lat={lat}&lon={lon}&units=metric&appid={app_id}')
        current = resp['current']
        temp = current['temp']
        feels_like = current['feels_like']
        answer = f'Now {temp}C feels like {feels_like}C'
        await message.answer(answer)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()
