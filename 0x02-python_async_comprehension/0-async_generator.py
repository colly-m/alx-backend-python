#!/usr/bin/env python3
"""Module to write a coroutine called async_generator"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function to yeild random float numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield(uniform(0, 10))
