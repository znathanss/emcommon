#!/usr/bin/env python3

from emcommon.common import esi_request
import requests
import json
import redis
from urllib.parse import urljoin


class Universe:
    def __init__(self, redis_conn=False):
        self.redis_conn = redis_conn
        self.base_url = "https://esi.evetech.net/latest/universe/"

    def systems(self):
        request_url = urljoin(self.base_url, 'systems')
        data = json.loads(esi_request(request_url, "GET"))
        return data