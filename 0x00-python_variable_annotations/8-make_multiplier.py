#!/usr/bin/env python3
"""Module to return a multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function to return a function thut multiplies a float by a float"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
