#!/usr/bin/env python3
import asyncio
from typing import List
import random

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns the list of delays in ascending order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create tasks using task_wait_random

    completed_tasks = []
    for task in asyncio.as_completed(tasks):
        completed_tasks.append(await task)  # Collect completed task results as they finish

    return completed_tasks  # Return the list of delays

