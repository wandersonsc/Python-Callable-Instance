import pytest
import socket
from simple_cache import Cache


def test_cache():

    host = socket.gethostbyname("www.google.com")
    cache = Cache()

    assert host in cache(host)

    # www.google.com': '172.217.28.228
