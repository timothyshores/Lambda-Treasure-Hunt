from random import choice
from time import sleep
from server_actions import *
from support import *


# Setup in case Treasure Hunt Section is skipped
data = get_init()
print('data', data)
map = file_to_json('full_map.txt')
sleep(1)
coins_mined = 0

# Treasure Hunt
# while get_status()['gold'] < 1000:
#     data = treasure_hunt()
#     data = move_to_location(data['room_id'], KEY_ROOMS['Shop'], data, map)
#     data = shop_check(data)
# print('Treasure Hunt Complete')

# # Name Change
# print(f'Moving to Pirate Rys room')
# data = move_to_location(data['room_id'], KEY_ROOMS["Pirate Ry's"], data, map)
# data = change_name('Christian Allen')
# print('Name Change Complete')

# Finding Mine Location
# print('Moving to the wishing well')
# data = move_to_location(data['room_id'], KEY_ROOMS['Wishing Well'], data, map)
# print('Getting the message from the well...')
# get_binary_from_well()
# message = translate_binary('binary.txt')
# print(message)

# Mining - Incomplete
# mine_location = int(message[-3:])
# print('Moving to mine')
# data = move_to_location(data['room_id'], mine_location, data, map)
# print('In the mine')

message = []
response = {'cooldown': -1}
while message == []:
    sleep(response['cooldown']+1)
    data = get_last_proof()
    print('data', data)
    proof = data['proof']
    leading_zeros = data['difficulty']

    while True:
        print('get_balance()', get_balance())
        new_proof = proof_of_work(proof, leading_zeros)
        response = mine(new_proof)  # DICTIONARY
        print("response", response)
        message = response['messages']
        print('message', message)
        sleep(response["cooldown"] + 1)
        print(get_balance())
