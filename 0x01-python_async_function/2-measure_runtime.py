#!/usr/bin/env python3
import time
import asyncio
from typing import List
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))

    completed_delays = []
    for task in asyncio.as_completed(delays):
        delay = await task
        completed_delays.append(delay)

    return completed_delays


def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Call wait_n and wait for its completion
    end_time = time.time()  # Record the end time
    
    total_time = end_time - start_time  # Calculate total elapsed time
    return total_time / n  # Return the average time per coroutine

