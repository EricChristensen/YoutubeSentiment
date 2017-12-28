from src import api

def test_get_comments():
    assert api.get_comments("url") != ""
