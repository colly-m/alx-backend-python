#!/usr/bin/env python3
"""Module to take list of ints and floats to return sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function to take a listof ints and floats and return float sum"""
    return sum(mxd_lst)
