#!/usr/bin/env python3
"""Module to create a class to inherit from utils.access_nested_map"""
import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """Function to access nested maps"""
    curr = nested_map
    for key in path:
        curr = curr[key]
    return curr


class TestAccessNestedMap(unittest.TestCase):
    """Class to inherit from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Function to check the outcome using test"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
