#!/usr/bin/env python3
"""Module for an asynchronous coroutine that waits for a random delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Funtion to generate a random num then returns it after a delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
