#!/usr/bin/env python3
"""Module to test client"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})

    def test_org(self, org_name, mock_get_json):
        """Function to test GithubOrgClient.org returning the correct value"""
        client = GithubOrgClient(org_name)
        result = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"

        mock_get_json.assert_called_once_with(expected_url)

        self.assertEqual(result, {"login": "mocked_org"})

    def test_public_repos_url(self):
        """Function to test GithubOrgClient._public_repos_url returns the expected value"""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': 'https://api.github.com/orgs/google/repos'}
            client = GithubOrgClient('google')
            result = client._public_repos_url

            self.assertEqual(result, 'https://api.github.com/orgs/google/repos')
