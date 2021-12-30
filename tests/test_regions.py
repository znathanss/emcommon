#!/usr/bin/python3

from emcommon.regions import Region

def test_region_pages():
    pages = int(Region(10000002).market_pages())
    assert pages > 0