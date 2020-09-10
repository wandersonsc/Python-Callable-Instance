import pytest
from simple_cache import Cache


def test_cache():

    host = "www.google.com"
    cache = Cache()

    assert "172.217.28.228" in cache(host)

    # www.google.com': '172.217.28.228
