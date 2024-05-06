#!/usr/bin/env python3
"""Module to alter a new function"""
import asyncio
from typing import List
from random import uniform


async def task_wait_random(max_delay: int) -> float:
    """Function to return float variables while delayed"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function to return a list of float variables in ascention order
    without using sort() because of concurrency
    """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
