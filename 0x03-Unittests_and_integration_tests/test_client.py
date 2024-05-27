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

    def test_public_repos_url(self, name, outcome):
        """Function to test GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=outcome)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, outcome.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Function to test in github for public_repos return repo list"""
        mock_get_json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'}
        ]

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value =
            'https://api.github.com/orgs/google/repos'
            client = GithubOrgClient('google')
            result = client.public_repos()

            self.assertEqual(result, [{'name': 'repo1'}, {'name': 'repo2'}])
            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                    'https://api.github.com/orgs/google/repos')
