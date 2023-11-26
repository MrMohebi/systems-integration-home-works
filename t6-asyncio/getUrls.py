import requests
import asyncio
import aiohttp

async def getUrl(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    t1 = asyncio.create_task(getUrl('https://google.com'))
    t2 = asyncio.create_task(getUrl('https://ifconfig.io'))
    t3 = asyncio.create_task(getUrl('https://bing.com'))

    response1 = await t1
    print(response1)
    response2 = await t2
    print(response2)
    response3 = await t3
    print(response3)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

