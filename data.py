import requests
import json
import os
from config import API_KEY

def fetch_api_data(url, params):
    params['key'] = API_KEY
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("FAILED")
        response.raise_for_status()


def loop_through_states():
    state_abbreviations = [
        'AL', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
        'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
        'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]
    for state in state_abbreviations:
        pull_data(state)
        

def filter_data(data):
    filtered_data = []
    with open('state_data.json', 'r') as f:
        state_data = json.load(f)
    dict_list = state_data['data']
    for item in dict_list:
        if item.get("short_desc") == "CORN - ACRES PLANTED":
            filtered_data.append(item)
    return filtered_data
def pull_data(state):
    params = {
        'commodity_desc': 'CORN',
        'year__GE': '2024',
        'state_alpha': state,
        'format': 'json'
    }
    url = "https://quickstats.nass.usda.gov/api/api_GET/"
    data = fetch_api_data(url, params)
    add_data_to_file(data, 'state_data.json')
    filtered_data = filter_data(data)
    data_list.append(filtered_data)


def add_data_to_file(data, filepath):
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    data_list = []
    pull_data('IA')
    add_data_to_file(data_list, 'crop_data.json')