#!/usr/bin/env python3
import asyncio
from async_generator import async_generator  # Corrected import statement

async def async_comprehension():
    return [num async for num in async_generator()]

