import asyncio
import re

import aiohttp
from lxml import etree

import exceptions
from db.database_functions import create_product_in_db


async def get_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            parser = etree.HTMLParser()
            tree = etree.HTML(html, parser)
            return tree


async def get_and_create_in_db_all_products(excel):
    row_info = []

    async def processing_row(row):
        title = row['title']
        url = row['url']
        page = await get_response(url)
        page_price = page.xpath(row['xpath'])[0]
        try:
            price = re.sub('[^0-9]', '', page_price)
        except TypeError:
            raise exceptions.NotNumberInXPathException

        create_product_in_db(title, url, price)
        row_info.append((title, url, price))

    tasks = [processing_row(row) for _, row in excel.iterrows()]
    await asyncio.gather(*tasks)

    return row_info
