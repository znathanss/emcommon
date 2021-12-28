from emcommon.items import Item
from emcommon.systems import System
from emcommon.universe import Universe
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'redis-master')
r = redis.Redis(host=redis_host, port=6379, db=0)

def test_universe_systems():
    eve = Universe()
    assert 30000142 in eve.systems()

def test_universe_regions():
    eve = Universe()
    assert 10000002 in eve.regions()

def test_universe_constellations():
    eve = Universe()
    assert 20000027 in eve.constellations()

def test_universe_structures():
    eve = Universe()
    assert len(eve.structures()) > 0