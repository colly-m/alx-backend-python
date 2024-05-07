#!/usr/bin/env python3
"""Module to write a coroutine async_comprehension"""
from typing import List, Generator
import asyncio
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Coroutine function to yeild random float numbers asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield(uniform(0, 10))


async def async_comprehension() -> List[float]:
    """Coroutine to collect 10 random numbers using async"""
    async_gen = async_generator()
    random_nums = [num async for num in async_gen]
    return random_nums
