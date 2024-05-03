#!/usr/bin/env python3
"""Module to correct duck typing"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function to correct duck-typed annotations"""
    if lst:
        return lst[0]
    else:
        return None
