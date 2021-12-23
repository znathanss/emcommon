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