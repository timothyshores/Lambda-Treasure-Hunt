import json
from time import sleep
from random import choice
from server_actions import *
from cpu import CPU
import hashlib
import random
from timeit import default_timer as timer


KEY_ROOMS = {"The Transmogriphier": 495,
             "The Peak of Mt. Holloway": 22,
             "Pirate Ry's": 467,
             "A brightly lit room": 0,
             "A Dark Cave": 488,
             "Linh's Shrine": 461,
             "Glasowyn's Grave": 499,
             "Wishing Well": 55,
             "Shop": 1}


def extract_room_info(data):
    room = {}
    room_descriptors = ['room_id', 'title', 'coordinates', 'description',
                        'terrain', 'elevation', 'exits', 'items']
    for value in room_descriptors:
        room[value] = data[value]

    return room


def make_blank_map(room_count=500):
    rooms = {}
    for i in range(room_count):
        rooms[i] = {"n": None, "s": None, "e": None, "w": None,
                    "title": None, "terrain": None, "elevation": None,
                    "coordinates": None, "description": None}

    return rooms


def find_unvisited_directions(exits, current_room):
    unvisited = []
    for direction in exits:
        if current_room[direction] is None:
            unvisited.append(direction)
    return unvisited


def json_to_file(data, file_name):
    print('Saving File...')
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)
    print('Save Complete')


def file_to_json(filename):
    with open(filename) as json_file:
        file = json.load(json_file)
    return file


def pickup_item_check(data):
    error = None
    while (data['items'] != []) and (not error):
        data = get_item({'name': data['items'][0]})
        error = data['errors']
        if not error:
            print('Picked up item')
        sleep(data['cooldown']+1)
    return data


def drop_item_check(data):
    status = get_status()
    if status['encumbrance'] > status['strength']:
        data = drop_item({'name': 'treasure'})
        print('Dropped Item')
        sleep(data['cooldown']+1)
    else:
        sleep(status['cooldown']+1)

    return data


def item_check(data):
    data = pickup_item_check(data)
    data = drop_item_check(data)
    return data


def find_path(start, end, map):
    best = None
    if start == end:
        return []
    while (best is None) or (len(best) > 250):
        path = []
        current_room = start
        while current_room != end:
            move = map[current_room][choice(['n', 's', 'e', 'w'])]
            if (move is not None):
                if (path == []) or (move != path[-1]):
                    path.append(current_room)
                    current_room = str(move)
                else:
                    current_room = path.pop()
        path.append(move)
        if (best is None) or (len(path) < len(best)):
            best = path
    return best


def trim_path(current_room, path):
    cut = 0
    for i in range(len(path)):
        if path[i] == current_room:
            cut = i
    return path[cut+1:]


def get_move(target_room, data, map):
    current_room = str(data['room_id'])
    exits = data['exits']

    for direction in exits:
        if map[current_room][direction] == int(target_room):
            return direction


def shop_check(data):
    if data['title'] == 'Shop':
        inventory = get_status()['inventory']
        for item in inventory:
            data = sell_item({'name': item, 'confirm': 'yes'})
            print('Sold Item')
            sleep(data['cooldown'] + 1)
        print('All items sold')
    return data


def move_to_location(current_room, destination, data, map):
    current_room = str(current_room)
    destination = str(destination)

    path = find_path(current_room, destination, map)
    while len(path) > 1:
        print(path)
        path = trim_path(current_room, path)
        move = str(get_move(path[0], data, map))
        data = make_move({'direction': move,
                          'next_room_id': str(map[current_room][move])})

        current_room = str(data['room_id'])
        sleep(data['cooldown'] + 1)
    return data


def list_to_file(data, filename):
    with open(filename, 'w') as filehandle:
        for line in data:
            filehandle.write('%s\n' % line)


def get_binary_from_well():
    binary = examine({'name': 'Wishing Well'})['description']
    binary = binary.split('\n')[2:]

    list_to_file(binary, 'binary.txt')


def translate_binary(filename):
    cpu = CPU()
    cpu.load(filename)
    return ''.join(cpu.run())


def treasure_hunt():
    map = file_to_json('full_map.txt')
    reverse = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}
    backtrack = []
    data = get_init()
    sleep(data['cooldown']+1)
    rooms = make_blank_map()
    inventory = get_status()['inventory']

    while len(inventory) < 5:
        current_room_id = data['room_id']
        print(f'Finding treasure in room: {current_room_id}')
        print(f'# of things in inventory: {inventory}')
        room_data = extract_room_info(data)

        data = item_check(data)
        exits = data['exits']
        valid_moves = find_unvisited_directions(exits, rooms[current_room_id])

        if valid_moves != []:
            move = choice(valid_moves)
            data = make_move({'direction': move,
                              "next_room_id": str(map[str(current_room_id)][move])})
            backtrack.append(reverse[move])
            rooms[current_room_id][move] = data['room_id']
            rooms[data['room_id']][reverse[move]] = current_room_id
        else:
            move = backtrack.pop(-1)
            data = make_move({'direction': move,
                              'next_room_id': str(map[str(current_room_id)][move])})

        sleep(data['cooldown']+1)
        inventory = get_status()['inventory']
    return data


def proof_of_work(last_proof, leading_zeros):

    start = timer()

    print("support.py proof_of_work()")
    proof = random.randint(0, 10000000)
    print(f'starting proof:{proof}')
    while valid_proof(last_proof, proof, leading_zeros) is False:
        proof += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_hash, proof, leading_zeros):
    # last_guess_hash = hashlib.sha256(str(last_hash).encode()).hexdigest()
    temp = f"{last_hash}{proof}"
    guess_hash = hashlib.sha256(temp.encode()).hexdigest()
    # print(guess_hash[:leading_zeros])
    # print('0'.zfill(leading_zeros))
    return guess_hash[:leading_zeros] == '0'.zfill(leading_zeros)
