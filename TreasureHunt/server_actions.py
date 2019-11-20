import requests


api_key = ''
url_base = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'
headers = {'Content-Type': 'application/json',
           'Authorization': 'Token ' + api_key}

def get_init():
    response = requests.get(url_base + 'init', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def get_status():
    response = requests.post(url_base + 'status', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def get_cooldown():
    return get_status()['cooldown']


def examine(target_json):
    response = requests.post(url_base + 'examine', headers=headers, json=target_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def make_move(move_json):
    response = requests.post(url_base + 'move', headers=headers, json=move_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def get_item(item_json):
    response = requests.post(url_base + 'take', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def drop_item(item_json):
    response = requests.post(url_base + 'drop', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def sell_item(item_json):
    room_title = get_init()['title']
    if room_title is not 'Shop':
        return 'You must be in the shop to sell items'

    response = requests.post(url_base + 'sell', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


