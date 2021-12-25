"""
systems type class
"""

import requests
import json
from emcommon.common import esi_request

class System:
    """ An eve online system type"""
    def __init__(self, systemID, redis_conn=False):
        self.systemID = systemID
        self.redis_conn = redis_conn


    def systemID(self):
        """ Just return the typeID """
        return self.systemID
    

    def info(self, field):
        """ Return the typeName for a given typeID"""
        if not self.redis_conn:
            request_url = "https://esi.evetech.net/latest/universe/systems/{}/?datasource=tranquility&language=en".format(self.systemID)
            data = json.loads(esi_request(request_url, "GET"))
            return data[field]
        cached_data = self.redis_conn.get('system_info_{}'.format(self.systemID))
        if cached_data is None:
            request_url = "https://esi.evetech.net/latest/universe/systems/{}/?datasource=tranquility&language=en".format(self.systemID)
            data = json.loads(esi_request(request_url, "GET"))
            self.redis_conn.setex('system_info_{}'.format(self.systemID), 3600, json.dumps(data))
            return data[field]
        cached_data = json.loads(cached_data.decode('utf-8'))
        return cached_data[field]