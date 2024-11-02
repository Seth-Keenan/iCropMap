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
        

def filter_data(data):
    filtered_data = []
    with open('state_data.json', 'r') as f:
        state_data = json.load(f)
    dict_list = state_data['data']
    for item in dict_list:
        if item.get("short_desc") == "CORN - ACRES PLANTED" and item.get("reference_period_desc") == "YEAR":
            new_item = {"crop": item.get("commodity_desc")}
            new_item["state"] = item.get("state_name")
            new_item["amount"] = item.get("Value")
            filtered_data.append(new_item)
    return filtered_data

def pull_data(crop, data_list):
    params = {
        'commodity_desc': crop,
        'year__GE': '2024',
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

def main(crop):
    data_list = []
    pull_data(crop, data_list)
    add_data_to_file(data_list, 'crop_data.json')
    
if __name__ == "__main__":
    main()