import asyncio
import logging
import time

import aiohttp

URL_BASE = 'https://api-users.onrender.com/populatedata/?qty=300'
logging.basicConfig(filename='requests.log', filemode='a', format='%(asctime)s - %(message)s',
                    level=logging.INFO)
logging.info(f'Start time')
start_time = time.time()


async def main():

    async with aiohttp.ClientSession() as session:

        for number in range(500):
            async with session.get(URL_BASE) as resp:
                body = await resp.text()
                logging.info(f'{body}')

asyncio.run(main())
logging.info(f'Elapsed time {time.time()} - {start_time}')
