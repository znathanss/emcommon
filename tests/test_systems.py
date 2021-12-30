#!/usr/bin/python3


from emcommon.items import Item
from emcommon.systems import System
import os


def test_system_system_id():
    item = System(30000142)
    assert item.system_id == 30000142

def test_system_planets():
    planets = System(30000142).info('planets')
    assert len(planets) > 0
