#!/usr/bin/env python3
"""Module to unittest a class to inherit from utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Class to inherit from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nest_map, path, expected):
        """Function to check the outcome using test"""
        self.assertEqual(access_nested_map(nest_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nest_map, path, error_error):
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


class TestMemoizer(unittest.TestCase):
    """Class function to test memoization"""
    def test_memoize(self):
        """Function to test memoization"""

        class TestClass:
            """Class for the test class"""

            def a_method(self):
                """Function to output 42"""
                return 42

            @memoize
            def a_property(self):
                """Function to get the memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
