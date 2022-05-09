import requests

def test_home():
    response=requests.get("http://127.0.0.1:8000/")
    actual=response.status_code
    expected=200
    assert actual==expected

def test_about():
    response=requests.get("http://127.0.0.1:8000/about")
    actual=response.status_code
    expected=200
    assert actual==expected