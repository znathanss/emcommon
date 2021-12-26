# -*- coding: future_fstrings -*-
"""
systems type class
"""

import json
from emcommon.common import esi_request


class System:
    """ An eve online system type"""
    def __init__(self, system_id, redis_conn=False):
        self.system_id = system_id
        self.redis_conn = redis_conn

    def info(self, field):
        """ Return the typeName for a given type_id"""
        if not self.redis_conn:
            request_url = f"https://esi.evetech.net/latest/universe/systems/{self.system_id}/?datasource=tranquility&language=en"
            data = json.loads(esi_request(request_url, "GET"))
            return data[field]
        cached_data = self.redis_conn.get(f'system_info_{self.system_id}')
        if cached_data is None:
            request_url = f"https://esi.evetech.net/latest/universe/systems/{self.system_id}/?datasource=tranquility&language=en"
            data = json.loads(esi_request(request_url, "GET"))
            self.redis_conn.setex(f'system_info_{self.system_id}', 3600, json.dumps(data))
            return data[field]
        cached_data = json.loads(cached_data.decode('utf-8'))
        return cached_data[field]
