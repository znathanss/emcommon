# -*- coding: future_fstrings -*-
"""
systems type class
"""

import json
import requests
from emcommon.common import esi_request


class Region:
    """ An eve online region type"""
    def __init__(self, region_id):
        self.region_id = region_id

    def info(self, field):
        """ Return the typeName for a given type_id"""
        request_url = f"https://esi.evetech.net/latest/universe/regions/{self.region_id}/?datasource=tranquility&language=en"
        data = json.loads(esi_request(request_url, "GET"))
        return data[field]

    def market_pages(self):
        """ Return the number of pages of market orders for this region """
        request_url = f"https://esi.evetech.net/latest/markets/{self.region_id}/orders/?datasource=tranquility&page=1"
        data = requests.get(request_url)
        return data.headers['x-pages']