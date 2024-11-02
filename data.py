import requests
import urllib.parse
import json
from config import API_KEY

def main(crop): # pass crop to get state, crop, and amount
    pull_data(crop)

def pull_data(crop):
    params = {
        'commodity_desc': crop,
        'year__GE': '2024',
        'key': API_KEY,
        'format': 'json',
        "short_desc": f"{crop} - ACRES PLANTED",
        "reference_period_desc": "YEAR"
    }
    encoded_params = urllib.parse.urlencode(params)
    base_url = "https://quickstats.nass.usda.gov/api/api_GET/"
    full_url = f"{base_url}?{encoded_params}"
    data = fetch_api_data(full_url, params) # pull data from API
    
    add_data_to_file(data, 'state_data.json') # add unfilitered data to json file
    filtered_data = filter_data(data)
    add_data_to_file(filtered_data, 'crop_data.json') # add filtered data to json file

def fetch_api_data(url, params):
    response = requests.get(url)
    if response.status_code == 200: # successful request
        return response.json()
    else:
        response.raise_for_status() # raise exception if request fails
        
def filter_data(data):
    filtered_data = []
    with open('state_data.json', 'r') as f: # open file of unfiltered json file 
        state_data = json.load(f)
    dict_list = state_data['data'] # list of dictionaries
    for item in dict_list: # loop through dictionaries
        if item.get("short_desc") == "CORN - ACRES PLANTED" and item.get("reference_period_desc") == "YEAR": # anything other then acres planted and ignores month data
            new_item = {"crop": item.get("commodity_desc")}
            new_item["state"] = item.get("state_name")
            new_item["amount"] = item.get("Value")
            # adds crop, state, and amount of acres of the crop planted per state to dictionary
            filtered_data.append(new_item)
    return filtered_data

def add_data_to_file(data, filepath): # add filtered data to file
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
if __name__ == "__main__":
    main('CORN') # passing CORN for testing reasons, needs to be a input per filter later