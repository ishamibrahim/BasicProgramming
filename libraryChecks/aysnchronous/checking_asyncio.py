#!/usr/bin/env python3
# !/usr/bin/env python3
# rand.py

import asyncio
import random

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
    print(c[idx] + f"---> Finished: makerandom({idx}) == {i}" + c[0])
    return idx


async def main1():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(4)))
    return res


# if __name__ == "__main__":
#     random.seed(444)
#     r1, r2, r3, r4 = asyncio.run(main1())
#     print(RESET) # Changing color to white
#     print(f"r1: {r1}, r2: {r2}, r3: {r3}, r4: {r4}")

##################################### Chaining coroutines ###########################

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

if __name__ == "__main__":
    import sys
    random.seed(555)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main2(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")

#################################
