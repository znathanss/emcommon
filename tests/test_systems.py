#!/usr/bin/python3


from emcommon.items import Item
from emcommon.systems import System
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'redis-master')
r = redis.Redis(host=redis_host, port=6379, db=0)


def test_system_systemID():
    item = System(30000142)
    assert item.systemID == 30000142

def test_system_planets():
    planets = System(30000142).info('planets')
    assert len(planets) > 0