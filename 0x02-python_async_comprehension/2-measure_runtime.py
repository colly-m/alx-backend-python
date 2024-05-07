#!/usr/bin/env python3
"""Module to write a coroutine that executes async_comprehension
four times"""
from typing import List, Generator
import asyncio
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """Coroutine to yield random float numbers asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """Coroutine to collect 10 random numbers using async"""
    async_gen = async_generator()
    random_nums = [num async for num in async_gen]
    return random_nums


async def measure_runtime() -> float:
    """
    Coroutine to measure the total runtime of async_comprehension
    executed four times in parallel"""
    start_time = asyncio.get_running_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
