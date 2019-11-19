import requests
import pprint
import pickle
import time
import json


# Load and print map from pickle
map = pickle.load(open("map.p", "rb"))
pp = pprint.PrettyPrinter(compact=True, indent=4)
print('\nInitial Map from Pickle: ')
pp.pprint(map)

# Read API key from local git ignored file
with open('api.txt', 'r') as reader:
    key = reader.read().strip()

# Global API variables
headers = {'Authorization': 'Token ' + key, 'Content-type': 'application/json'}
url = 'https://lambda-treasure-hunt.herokuapp.com/api/adv/'

# Initialize API and pretty print response from server
print("\nInitial API Call: ")
response = requests.get(url + 'init/', headers=headers).json()
pp.pprint(response)

# Set new key value pair in local map dictionary
map = {
    **map,
    response['room_id']: {exists: "?" for exists in response['exits']}
}

# Write initial API call to map pickle
pickle.dump(map, open("map.p", "wb"))

# PPretty print new map pickle
map = pickle.load(open("map.p", "rb"))
print('\n New Map Pickle: ')
pp.pprint(map)


print('\Waiting 15 second before next move... \n')
time.sleep(15)

response = requests.post(
    url + 'move/',
    headers=headers,
    json={"direction": "e"})

json = response.json()

print("\nNew room: ")
pp.pprint(json)

map = {
    **map,
    response['room_id']: {exists: "?" for exists in response['exits']}
}

print('map')
print(map)
