import asyncio
from unicodedata import category
import aiohttp


urls = [
        'http://127.0.0.1:8000/product/category/8', 
        'http://127.0.0.1:8000/product/category/9'
       ]


async def get_url(url):
    print(f'getting {url}')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            category_id = url.split('/')[-1]
            with open(f'category_{category_id}.html', 'w', encoding='utf-8') as f:
                f.write(data)


futures = [get_url(u) for u in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))

