import json
import requests
from decouple import config


# with open('countries.json') as json_file:
#     data = json.load(json_file)
#     for country in data['data']['countries']:
#         country_id = country['id']
#         country_name = country['label']
#         states = requests.get(
#             'https://www.universal-tutorial.com/api/states/' + country_name,
#             headers={
#                 'Authorization': 'Bearer ' + config('API_KEY),
#                 'Accept': 'application/json'
#             }
#         )



def get_states(country):
    states = requests.get(
            'https://www.universal-tutorial.com/api/states/' + country,
            headers={
                'Authorization': 'Bearer ' + config('API_KEY'),
                'Accept': 'application/json'
            }
        )
    return states.json()


def get_countries():
    with open('countries.json', 'r') as myfile:
        data = myfile.read()
    
    country_data = json.loads(data)
    return country_data


def write_file(countries):
    data = {}
    data['countries'] = []

    for country in countries:
        states = get_states(country['label'])
        data['countries'].append({
            'country_id': country['id'],
            'states': states
        })
    with open('states.json', 'w') as outfile:
        json.dump(data, outfile)


countries = get_countries()
write_file(countries['data']['countries'])