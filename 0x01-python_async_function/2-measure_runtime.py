#!/usr/bin/env python3
"""Module to measure total execution time ondelay"""
import asyncio
from typing import List
from random import uniform
import time


async def wait_random(max_delay: int) -> float:
    """Function to return float variable randomly with a delay"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function to return a list of float randomly from a delay"""
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays


def measure_time(n: int, max_delay: int) -> float:
    """Function to measure the total execution time for the delay"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
