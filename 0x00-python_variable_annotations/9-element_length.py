#!/usr/bin/env python3
"""Module to annotate a function's params and return values"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function to annotate params and return appropreate types"""
    return [(i, len(i)) for i in lst]
