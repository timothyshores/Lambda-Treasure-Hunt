import json


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
