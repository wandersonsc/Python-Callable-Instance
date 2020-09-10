import socket


class Cache:

    """ Model representation of the Cache Class """

    def __init__(self):

        self.cache = {}

    def __repr__(self):

        return f"{__class__.__name__}({self.cache})"

    def __call__(self, hostname, *args, **kwargs):

        if hostname not in self.cache:
            self.cache[hostname] = socket.gethostbyname(hostname)
        return self.cache[hostname]
