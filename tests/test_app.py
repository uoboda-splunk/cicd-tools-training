from app.app import get_info_string


def test_info_string():
    assert get_info_string() == "Hello, World!"
