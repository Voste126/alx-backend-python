#!/usr/bin/env python3
import asyncio
import time
from async_comprehension import async_comprehension  # Import async_comprehension from the previous task

async def measure_runtime():
    start_time = time.perf_counter()  # Record the start time

    # Run 4 instances of async_comprehension in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    total_time = time.perf_counter() - start_time  # Calculate the total runtime
    return total_time

