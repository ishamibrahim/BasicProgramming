#!/usr/bin/env python3
# !/usr/bin/env python3
# rand.py

import asyncio
import os
import pathlib
import random
import urllib.parse

import aiohttp

########################### Using async and await #######################################
# ANSI colors
c = (
    "\033[93m",  # orange
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)
RESET = "\033[0m" # White


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(c[idx] + f"Initiated makerandom({idx}).")
    i = random.randint(0, 10)
    while i <= threshold:
        print(c[idx] + f"makerandom({idx}) == {i} too low than {threshold}; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
        print(c[idx] + f"{i}")
    print(c[idx] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return idx


async def main1():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(4)))
    return res


# if __name__ == "__main__":
#     random.seed(44)
#     r1, r2, r3, r4 = asyncio.run(main1())
#     print(RESET) # Changing color to white
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}, r4: {r4}")

##################################### Chaining coroutines ###########################
#

import asyncio
import random
import time

async def part1(n: int) -> str:
    i = random.randint(0, 10)
    print(f"part1({n}) sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-1"
    print(f"Returning part1({n}) == {result}.")
    return result

async def part2(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"part2{n, arg} sleeping for {i} seconds.")
    await asyncio.sleep(i)
    result = f"result{n}-2 derived from {arg}"
    print(f"Returning part2{n, arg} == {result}.")
    return result

async def chain(n: int) -> None:
    start = time.perf_counter()
    p1 = await part1(n)
    p2 = await part2(n, p1)
    end = time.perf_counter() - start
    print(f"-->Chained result{n} => {p2} (took {end:0.2f} seconds).")

async def main2(*args):
    await asyncio.gather(*(chain(n) for n in args))

# if __name__ == "__main__":
#     import sys
#     random.seed(555)
#     args = [4, 8, 12] if len(sys.argv) == 1 else map(int, sys.argv[1:])
#     start = time.perf_counter()
#     asyncio.run(main2(*args))
#     end = time.perf_counter() - start
#     print(f"Program finished in {end:0.2f} seconds.")

################################# Using Queue ###################################

import itertools as it


async def makeitem(size):
    return os.urandom(size).hex()


async def randsleep(caller: str):
    i = random.randint(1, 5)
    print(f"{caller} Sleeping for {i} seconds")
    await asyncio.sleep(i)


async def produce(id: int, que: asyncio.Queue):
    n = random.randint(0, 2)
    print(f"number of times producer {id} is called: {n}")
    for _ in it.repeat(None, n):
        await randsleep(caller=f"Producer {id}")
        i = await makeitem(4)
        t = time.perf_counter()
        await que.put((i, t))
        print(f"Producer {id} added {i} to queue")


async def consume(id, que):
    while True:
        await randsleep(caller=f"Consumer: {id}")
        i, t = await que.get()
        now = time.perf_counter()
        print(f"Consumer {id} got element {i}. took {now-t:0.2f} seconds")
        que.task_done()


async def main3(pro_times, con_times: int):
    qu = asyncio.Queue()
    producers = [asyncio.create_task(produce(n, qu)) for n in range(pro_times)]
    consumers = [asyncio.create_task(consume(n, qu)) for n in range(con_times)]
    await asyncio.gather(*producers)
    await qu.join()
    print("all tasks are processed")
    for cr in consumers:
        cr.cancel()
    for pr in producers:
        pr.cancel()

# asyncio.run(main3(6, 3))

#################################3 Async generator ################################3

import asyncio

async def async_generator():
    for i in range(6):
        await asyncio.sleep(1)
        yield i

async def main4():
    async for value in async_generator():
        print(f"Received value: {value}")
    print("all done")

# asyncio.run(main4())

##################### Using explicit event loop################
# Instead of running via asyncio.run(), you can explicitly get the event loop and run an async function

# g = asyncio.get_event_loop()
# try:
#     g.run_until_complete(main3(2, 6))
# finally:
#     g.close()

###################  A meaningful python program for unpredicatble http response times##########
from aiohttp import ClientSession
import aiofiles
import aiohttp
import logging
import re
logger = logging.getLogger('asyncUrl')
logging.getLogger("chardet.charsetprober").disabled = True
HREF_RE = re.compile('href="(.*?)"')


async def fetch_html(url: str, session: ClientSession) :
    resp = await session.request(method="GET", url= url)
    resp.raise_for_status()
    logger.info(f"Received response {resp.status} for url - {url}")
    html = await resp.text()
    return html

async def parse_url(url, session):
    found_set = set()
    try:
        html = await fetch_html(url, session)
    except (aiohttp.ClientError, aiohttp.http_exceptions.HttpProcessingError) as err:
        logger.error(f"AIOHTTP ERROR: parsing for {url} failed due to error: {err}")
        return found_set
    except Exception as e:
        logger.error(f"NON AIOHTTP ERROR: parsing for {url} failed due to error: {e}")
        return found_set
    else:
        for link in HREF_RE.findall(html):
            try:
                abslink = urllib.parse.urljoin(url, link)
            except (urllib.error.URLError, ValueError) as e:
                logger.exception(f"Error parsing url - {e}")
                continue
            else:
                found_set.add(abslink)
        logger.info(f"Found {len(found_set)} links for url: {url}")
        return found_set


async def write_one(file, url, session):
    result = await parse_url(url, session=session)
    if not result:
        return None
    async with aiofiles.open(file, 'a') as outfile:
        for p in result:
            await outfile.write(f"{url},\t{p}\n")
        logger.info(f"wrote result for url {url}")


async def crawl_for_urls_in_bulk(url_list, outfile):
    async with ClientSession() as session:
        tasks = []
        for url in url_list:
            tasks.append(
                asyncio.create_task(write_one(file=outfile, url=url, session=session))
            )
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    here = pathlib.Path(__file__).parent
    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("foundurls.csv")
    with open(outpath, 'w') as outfile:
        outfile.write("sourced_url,\tparsedurl\n")

    asyncio.run(crawl_for_urls_in_bulk(url_list=urls, outfile=outpath))
