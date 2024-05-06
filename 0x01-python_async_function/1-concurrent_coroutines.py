#!/usr/bin/env python3
"""Module to take 2 ints and spawn wait_random n times with specified delays"""
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """Function to return float variables while delayed"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function to return a list of float values in ascending order without using
    sort() because of concurrency
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
