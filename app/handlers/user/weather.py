import json
from datetime import datetime

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
                    timezone = 'Asia/Yekaterinburg'
                    timezone_offset = 5 * 60 * 60
        resp = await fetch(session, f'{base_url}lat={lat}&lon={lon}&units=metric&timezone_offset={timezone_offset}&timezone={timezone}&appid={app_id}')

        # current
        current = resp['current']
        temp = current['temp']
        feels_like = current['feels_like']
        weather_list = current['weather']
        weather_result = []
        for weather in weather_list:
            weather_result.append(weather['main'])

        # hourly
        hourly_list = resp['hourly']
        hour_result = ''
        for hour in hourly_list[1:9]:
            local_time = hour['dt'] + timezone_offset
            hour_temp = hour['temp']
            hour_weather_list = hour['weather']
            hour_weather_result = []
            for hour_weather in hour_weather_list:
                hour_weather_result.append(hour_weather['main'])
            f_hour = datetime.utcfromtimestamp(local_time).strftime('%H:%M')
            hour_result += f'{f_hour} - {hour_temp}c - {hour_weather_result}\n'

        answer = f'Now {temp}c feels like {feels_like}c {weather_result} \n{hour_result}'
        await message.answer(answer)


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()
