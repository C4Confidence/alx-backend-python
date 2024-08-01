#!/usr/bin/env python3
"""Use mypy to validate the following piece of code
and apply any necessary changes.
"""


from typing import TypeVar, Dict, Optional

T = TypeVar('T')

def safely_get_value(dct: Dict[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """More involved type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
