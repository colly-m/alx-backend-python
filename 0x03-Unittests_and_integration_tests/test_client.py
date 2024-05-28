#!/usr/bin/env python3
"""Module to test client"""
import fixtures
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized_class
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Function to test if client has_license returns the expected value"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class to test githubclient integration"""
    @classmethod
    def setUpClass(cls):
        """Function for patching 'requests.get' and returns example payloads
        found in the fixtures.
        """
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == cls.org_payload["repos_url"]:
                response = MagicMock()
                response.json.return_value = cls.repos_payload
                return response
            elif url.startswith("https://api.github.com/orgs/"):
                response = MagicMock()
                response.json.return_value = cls.org_payload
                return response
            return MagicMock()

        cls.mock_get.side_effect = side_effect
