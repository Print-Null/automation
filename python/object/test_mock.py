import mock
import pytest
from pytest_mock import mocker
from python.object.mock_study import invoke_mock_request


def test_get_foo(mocker):
    mocker.patch('python.object.mock_study.mock_request', return_value=300)
    assert invoke_mock_request("http://www.baidu.com") == 300


def test_get_foo2():
    with mock.patch('python.object.mock_study.mock_request', side_effetc=400) as mock_foo:
        assert invoke_mock_request("http://www.baidu.com") == mock_foo.return_value


@mock.patch('python.object.mock_study.mock_request', return_value=700)
def test_get_foo3(mock_request):
    assert invoke_mock_request("http://www.baidu.com") == mock_request.return_value
