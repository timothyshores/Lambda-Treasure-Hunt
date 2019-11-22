from random import choice
from time import sleep
from server_actions import *
from support import *

world_map = file_to_json('map.txt')
reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
backtrack = []
rooms_visited = 1
data = get_init()
rooms = make_blank_map()
sleep(data['cooldown']+1)

while rooms_visited < 500:
    current_room_id = data['room_id']
    room_data = extract_room_info(data)

    for key in room_data:
        rooms[current_room_id][key] = room_data[key]

    error = None
    while (data['items'] != []) and (not error):
        data = get_item({'name': data['items'][0]})
        error = data['errors']
        if not error:
            print('Picked up item')
        sleep(data['cooldown']+1)

    if data['title'] is 'Shop':
        inventory = get_status()['inventory']
        for item in inventory:
            data = sell_item({'name': item, 'confirm': 'yes'})
            print('Sold Item')
            sleep(data['cooldown']+1)
        print('All items sold')

    exits = data['exits']
    valid_moves = find_unvisited_directions(exits, rooms[current_room_id])

    if valid_moves != []:
        move = choice(valid_moves)
        data = make_move({'direction': move,
                          "next_room_id": str(world_map[str(current_room_id)][move])})
        backtrack.append(reverse[move])
        rooms[current_room_id][move] = data['room_id']
        rooms[data['room_id']][reverse[move]] = current_room_id
        rooms_visited += 1
        print(rooms_visited)
    else:
        move = backtrack.pop(-1)
        data = make_move({'direction': move,
                          'next_room_id': str(world_map[str(current_room_id)][move])})

    sleep(data['cooldown']+1)

json_to_file(rooms, 'full_map.txt')


# NEED TO ADD CHANGE_PLAYER_NAME ROOM
# NEED TO ADD MINING ROOM
