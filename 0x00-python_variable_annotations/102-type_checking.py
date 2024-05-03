#!/usr/bin/env python3
"""Module to validate a piece of code and apply changes"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """Function to make the changes into the code"""
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for i in range(factor)
    )
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
