import asyncio
import json

import aioredis


async def main():
    redis = await aioredis.create_redis_pool('redis://redis')
    with open('city.list.json', 'r') as f:
        city_list = json.load(f)
        for city in city_list:
            await redis.hmset_dict(
                city['name'],
                lon=city['coord']['lon'],
                lat=city['coord']['lat'],
            )

    redis.close()
    await redis.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
