import json
import redis
import requests
from emcommon.common import esi_request


def get_typeName(typeID, redis_conn=None):
    """ Return the typeName for a given typeID"""
    request_url = "https://esi.evetech.net/latest/universe/names/?datasource=tranquility"
    request_body = [typeID]
    if not redis_conn:
        item_data = esi_request(request_url, "POST", request_body)
        for item in item_data:
            if item_data['category'] == "inventory_type":
                return int(item_data['id'])
    if redis_conn:
        cached_answer = redis_conn.get('type_name_{}'.format(typeID))
        if cached_answer is None:
            item_data = esi_request(request_url, "POST", request_body)
            for item in item_data:
                if item_data['category'] == "inventory_type":
                    redis_conn.set('type_name_{}'.format(typeID), item_data['name'])
                    return item_data['name']


        

    


def get_type_ids():
    """
    Return a json object of all typeIDs currently in the SDE
    """
    answer = {}
    r = redis_connect()
    cached_data = r.get('all_type_ids')
    if not cached_data:
        sql = "select typeID, typeName from invTypes"
        conn = mysql_connect()
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        r.setex(
            'all_type_ids',
            3600,
            json.dumps(results)
        )
        for row in results:
            answer[row['typeName']] = row['typeID']
        return jsonable_encoder(answer)
    else:
        results = cached_data
    for row in json.loads(results):
        answer[row['typeName']] = row['typeID']
    return answer


def get_type_ids():
    """
    Return a json object of all typeIDs currently in the SDE
    """
    answer = {}
    r = redis_connect()
    cached_data = r.get('all_tradeable_type_ids')
    if not cached_data:
        sql = "select typeID, typeName from invTypes where marketGroupID is not NULL"
        conn = mysql_connect()
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        r.setex(
            'all_tradeable_type_ids',
            3600,
            json.dumps(results)
        )
        for row in results:
            answer[row['typeName']] = row['typeID']
        return jsonable_encoder(answer)
    else:
        results = cached_data
    for row in json.loads(results):
        answer[row['typeName']] = row['typeID']
    return answer


def get_item_id(item_name):
    """ Get the typeID for a given typeName """
    try:
        if item_name.isnumeric():
            return int(item_name)
    except:  # already an INT
        return item_name
    r = redis_connect()
    cached_answer = r.get('type_name_%s' % item_name)
    if cached_answer is None:
        conn = mysql_connect()
        cur = conn.cursor()
        sql = "select typeID from invTypes where typeName = '%s'" % item_name.strip()
        cur.execute(sql)
        result = cur.fetchone()
        type_id = result['typeID']
        r.setex('type_name_%s' % item_name, 3600, type_id)
    else:
        type_id = cached_answer
        return int(type_id)
