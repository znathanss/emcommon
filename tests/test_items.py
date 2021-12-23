#!/usr/bin/python3


from emcommon.items import get_typeName
import redis


r = redis.Redis(host='localhost', port=6379, db=0)

def test_get_typeName():
    assert get_typeName(34) == 'Tritanium'

def test_get_typeName_redis():
    assert get_typeName(34, r) == 'Tritanium'