import requests

def process_http_code(response):
    """
    Process the HTTP code of the response
    """
    if not response.ok:  # Save time by only looping if not 2xx
        if response.status_code == 400:
            print("Bad request")
            return False
        if response.status_code == 404:
            print("Not found")
            return False
        if response.status_code == 420:
            print("Rate limit exceeded")
            return False
        if response.status_code == 500:
            print("Internal server error")
            return False
        if response.status_code == 503:
            print("Service unavailable")
            return False
        if response.status_code == 504:
            print("Gateway timeout")
            return False
    if response.ok:
        return response


def esi_request(url, req_type, body=None):
    """
    Make an ESI request
    """
    headers = {
        'User-Agent': 'EVE-Market-Data-Tool/1.0',
    }
    if req_type == "GET":
        response = requests.get(url, headers=headers)
    elif req_type == "POST":
        response = requests.post(url, headers=headers, json=body)
    if process_http_code(response):
        return response.json()
    return False
    