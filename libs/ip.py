#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://stackoverflow.com/questions/691045/how-do-you-determine-if-an-ip-address-is-private-in-python

from struct import unpack
from socket import AF_INET, inet_pton


def lookup(ip):
    f = unpack('!I', inet_pton(AF_INET, ip))[0]
    private = (
        [2130706432, 4278190080],
        [3232235520, 4294901760],
        [2886729728, 4293918720],
        [167772160, 4278190080],
    )
    for net in private:
        if (f & net[1]) == net[0]:
            return True
    return False


def IPv4_to_int(s):
    return reduce(lambda a, b: a << 8 | b, map(int, s.split(".")))


def int_to_IPv4(ip):
    return ".".join(map(lambda n: str(ip >> n & 0xFF), [24, 16, 8, 0]))


if __name__ == '__main__':
    print(lookup("127.0.0.1"))
    print(lookup("192.168.10.1"))
    print(lookup("10.10.10.10"))
    print(lookup("172.17.255.255"))
