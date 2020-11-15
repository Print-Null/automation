import requests


def mock_request(url):
    return requests.get(url).status_code


def invoke_mock_request(url):
    return mock_request(url)
