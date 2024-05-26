#!/usr/bin/env python3
"""Module to create a class to inherit from utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, path


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, error_error):
        """Function to create an exception and ensure a KeyError is raised"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(error_output, e.exception)


class TestGeJson(unittest.TestCase):
    """Class to test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Function to test check the output"""
        mock_answer = Mock()
        mock_answer.json.return_value = test_payload
        with patch('requests.get', return_value=mock_answer):
            real_answer = get_json(test_url)
            self.assertEqual(real_answer, test_payload)
            mock_answer.json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
