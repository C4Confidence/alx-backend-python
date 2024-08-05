#!/usr/bin/env python3
"""An asyncrhronous coroutine that takes an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay btw 0 and max_delay secs and returns delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
