# import requests
from app.app import get_info_string


def test_info_string():
    assert get_info_string() == "Hello, Splunkers!"


# def test_with_container():
#     response = requests.get("http://localhost:8000")
#     assert response.status_code == 200
#     assert response.text == "Hello, World!"
