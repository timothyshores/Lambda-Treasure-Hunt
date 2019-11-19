import requests
import pprint

with open('api.txt', 'r') as reader:
    key = reader.read().strip()

# Initialization - Test your API key with the init command
response = requests.get(
    'https://lambda-treasure-hunt.herokuapp.com/api/adv/init/', headers={
        'Authorization': 'Token ' + key,
    }).json()

# Initialize pretty printer and print response from server
pp = pprint.PrettyPrinter(compact=True, indent=4)
pp.pprint(response)

map = {
    response['room_id']: {exists: "?" for exists in response['exits']}
}
