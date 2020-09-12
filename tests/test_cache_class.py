import pytest
import socket
from simple_cache import Cache


@pytest.fixture(scope="module")
def cache():
    cache = Cache()
    return cache


def test_cache(cache):

    host = socket.gethostbyname("www.google.com")
    assert host in cache(host)

    # www.google.com': '172.217.28.228


def test_clean_cache(cache):
    """ Teste the clean cache method """

    host = socket.gethostbyname("www.travis-ci.org")
    cache(host)
    cache.clear_cache()

    assert cache.search_host(host) is False


def test_search_host(cache):
    """ Teste the search host method """

    host = socket.gethostbyname("www.github.com")
    cache(host)

    assert cache.search_host(host) is True


def test_print_all_host_names(cache):
    """ Teste the search host method """

    host = socket.gethostbyname("www.facebook.com")
    cache(host)

    assert host in cache.get_all_host()
