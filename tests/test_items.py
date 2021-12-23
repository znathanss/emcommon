#!/usr/bin/python3


from emcommon.items import get_typeName, get_typeID
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'redis-master')
r = redis.Redis(host=redis_host, port=6379, db=1)

def test_get_typeName():
    assert get_typeName(34) == 'Tritanium'

def test_get_typeName_redis():
    assert get_typeName(34, r) == 'Tritanium'

def test_get_typeID():
    assert get_typeID('Tritanium') == 34

def test_get_typeID_redis():
    assert get_typeID('Tritanium', r) == 34