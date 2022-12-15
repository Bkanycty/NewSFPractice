import aiohttp
import asyncio


async def main():
    smile = '&#9786;'
    text = f'Какой-то текст {smile}'
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/news', data=text) as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(main())
