#!/usr/bin/python3


from emcommon.items import Item
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
    assert len(orders['sell_orders']) > 0

def test_Item_buy_orders():
    orders = Item(34, r).orders()
    assert len(orders['buy_orders']) > 0

def test_Item_sell_orders_jita():
    orders = Item(34, r).orders(30000142)
    assert len(orders['sell_orders']) > 0

def test_Item_buy_orders_jita():
    orders = Item(34, r).orders(30000142)
    assert len(orders['buy_orders']) > 0

def test_Item_price():
    price = Item(34, r).price()
    print(price)
    assert price > 0