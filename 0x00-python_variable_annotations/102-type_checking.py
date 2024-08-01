#!/usr/bin/env python3
"""More involved"""


from typing import List, Tuple, Union


"""Use MYPY to validate the following piece of code"""


def zoom_array(lst: Union[List[int], Tuple[int, ...]], factor: int = 2) -> List[int]:
    """Corrected annotations"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
