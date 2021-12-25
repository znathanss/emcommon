#!/usr/bin/python3


from emcommon.items import Item
from emcommon.systems import System
import redis
import os

redis_host = os.environ.get('REDIS_HOST', 'redis-master')
r = redis.Redis(host=redis_host, port=6379, db=0)


def test_Item_typeID():
    item = Item(34)
    assert item.typeID == 34

def test_Item_typeName():
    typeName = Item(34).info('name')
    assert typeName == 'Tritanium'

def test_Item_typeName_with_redis():
    typeName = Item(34, r).info('name')
    assert typeName == 'Tritanium'

def test_Item_typeID_info():
    typeName = Item(34).info('type_id')
    assert typeName == 34

def test_Item_typeID_info_with_redis():
    typeName = Item(34, r).info('type_id')
    assert typeName == 34

def test_Item_sell_orders():
    orders = Item(34, r).orders()
    assert len(orders) > 0

def test_Item_buy_orders():
    orders = Item(34, r).orders()
    assert len(orders) > 0

def test_Item_sell_orders_jita():
    orders = Item(34, r).orders(30000142)
    assert len(orders) > 0

def test_Item_buy_orders_jita():
    orders = Item(34, r).orders(30000142)
    assert len(orders) > 0

def test_all_minerals_prices():
    minerals = [
        34, 35, 36, 37, 38, 39, 40,
    ]
    for mineral in minerals:
        price = Item(mineral, r).price()
        print(price)
        assert price > 0

def test_system_systemName():
    typeName = System(30000142).info('name')
    assert typeName == 'Jita'

def test_system_systemID_with_redis():
    typeName = System(30000142, r).info('name')
    assert typeName == 'Jita'

def test_system_planets():
    planets = System(30000142).info('planets')
    assert len(planets) > 0

def test_system_planets_with_redis():
    planets = System(30000142, r).info('planets')
    assert len(planets) > 0