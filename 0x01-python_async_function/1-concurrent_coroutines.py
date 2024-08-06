#!/usr/bin/env python3
"""An async routine that spawn wait_random n times with specified max_delay."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times wit specified max_delay, return all delays."""
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        # Insert delay into the correct position to maintain ascending order
        if not delays:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
            else:
                delays.append(delay)
    return delays
