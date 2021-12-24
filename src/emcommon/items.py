"""
inventory type class
"""

import requests
import json
from emcommon.common import esi_request

class Item:
    """ An eve online inventory type"""
    def __init__(self, typeID, redis_conn=False):
        self.typeID = typeID
        self.redis_conn = redis_conn


    def typeID(self):
        """ Just return the typeID """
        return self.typeID


    def info(self, field):
        """ Return the typeName for a given typeID"""
        if not self.redis_conn:
            request_url = "https://esi.evetech.net/latest/universe/types/{}/?datasource=tranquility&language=en".format(self.typeID)
            data = json.loads(esi_request(request_url, "GET"))
            return data[field]
        cached_data = self.redis_conn.get('type_info_{}'.format(self.typeID))
        if cached_data is None:
            request_url = "https://esi.evetech.net/latest/universe/types/{}/?datasource=tranquility&language=en".format(self.typeID)
            data = json.loads(esi_request(request_url, "GET"))
            self.redis_conn.setex('type_info_{}'.format(self.typeID), 3600, json.dumps(data))
            return data[field]
        cached_data = json.loads(cached_data.decode('utf-8'))
        return cached_data[field]
    

    def orders(self, system_id=None):
        """ Return a list of orders for this typeID"""
        if system_id == None:
            request_url = "https://api.eve-market.net/orders?item_id={}".format(self.typeID)
        else:
            request_url = "https://api.eve-market.net/orders?item_id={}&system_id={}".format(self.typeID, system_id)
        data = json.loads(requests.get(request_url).text)
        return data


    def price(self, system_id=30000142):
        """ Return the price for this typeID. Defaults to Jita """
        request_url = "https://api.eve-market.net/get_adjusted_market_price?typeID={}&market={}".format(self.typeID, system_id)
        data = json.loads(requests.get(request_url).text)
        return data