import requests
from requests import Session

proxies = {
    "http": "http://127.0.0.1:8998",
    "https": "https://127.0.0.1:8998"
}

url_get = "https://httpbin.testing-studio.com/get"
url_post = "https://httpbin.testing-studio.com/post"


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    print(r.status_code)
    print(r.json())


def test_get():
    r = requests.get(url_get, headers={"user-agent": "firefox"}, params={"a": 1, "b": 2})
    print(r.json())
    print("-----------------------我是可爱的分割线------------------------")
    print(r.headers, end='\n')
    assert r.status_code == 200


def test_post():
    r = requests.post(url_post,
                      headers={"user-agent": "chrome"},
                      params={"a": 1, "b": 2, "c": 3},
                      data={"x": 100, "y": 200, "z": "baba"},
                      proxies=proxies,
                      verify=False
                      )
    print(r.json())
    assert r.status_code == 200
    assert r.json()['headers']['User-Agent'] == 'chrome'


def test_upload():
    r = requests.post(url_post,
                      files={"file": open(r"D:\MyProjects\test_appium\page\search.yaml", "rb")},
                      data={"x": 100, "y": 200},
                      headers={"user-agent": "chrome"},
                      cookies={"username": "requests", "password": "123456"},
                      proxies=proxies,
                      verify=False
                      )
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["Cookie"] == "password=123456; username=requests"
    print("-----------------------我是可爱的分割线------------------------")
    print(r.cookies, r.request)


def test_session():
    s = Session()
    s.proxies = proxies
    s.verify = False
    s.get(url_get, params={"m": "python", "n": "java"})
