#!/usr/bin/env python3
"""Module to add type annotations to functions"""
from typing import Mapping, TypeVar, Union, Any


T = TypeVar('T')
V = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D = None) -> V:
    """Function to get the value from a dictionary using the key"""
    if key in dct:
        return dct[key]
    else:
        return default
