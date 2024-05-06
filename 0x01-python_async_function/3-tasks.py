#!/usr/bin/env python3
"""Module to create an async function using function syntax"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Function to return variables with a delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay):
    """Function to create a task for the scheduler"""
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
