import requests
from time import sleep


api_key = 'faaab3b37b27f295ad78a62c727527fd032223a5'
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
    response = requests.post(url_base + 'examine', headers=headers,
                             json=target_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def make_move(move_json):
    response = requests.post(url_base + 'move', headers=headers,
                             json=move_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def change_name(name):
    response = requests.post(url_base + 'change_name', headers=headers,
                             json={'name': name, 'confirm': 'aye'})
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def get_item(item_json):
    response = requests.post(
        url_base + 'take', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def drop_item(item_json):
    response = requests.post(
        url_base + 'drop', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def sell_item(item_json):
    room_title = get_init()['title']
    if room_title != 'Shop':
        return 'You must be in the shop to sell items'

    sleep(1)
    response = requests.post(
        url_base + 'sell', headers=headers, json=item_json)
    status_code = response.status_code

    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()


def get_last_proof():
    response = requests.get(url_base[:-4] + 'bc/last_proof', headers=headers)
    status_code = response.status_code

    if status_code is not 200:
        return status_code
    return response.json()


def mine(proof):
    print(f'mine proof:{proof}')
    response = requests.post(
        url_base[:-4] + 'bc/mine', headers=headers, json={"proof": proof})
    print('server_actions.py mine response ', response.json())
    # status_code = response.status_code

    # if status_code is not 200:
    #     return status_code
    return response.json()


def get_balance():
    response = requests.get(url_base[:-4] + 'bc/get_balance', headers=headers)
    status_code = response.status_code
    if status_code is not 200:
        return ('Unsuccessful Connection, Status Code:', status_code)
    return response.json()
