import asyncio
import json

import aiofiles


async def dr():
    async with aiofiles.open('dr.json', "r", encoding="utf-8") as file:
        content = await file.read()
        data = json.loads(content)
        if '6.3' in data:
            print(data['6.3'])


asyncio.run(dr())