import requests
import urllib.parse
import json
import pandas as pd
from config import API_KEY

class Crop:
    def __init__(self, crop, date):
        self.crop = crop
        self.date = date
        self.data = self.pull_data(crop, date)

    def pull_data(self, crop, date):
        params = {
            'commodity_desc': crop,
            'year': date,
            'key': API_KEY,
            'format': 'json',
            'freq_desc': "Annual",
            "short_desc": f"{crop} - ACRES PLANTED",
            "reference_period_desc": "YEAR"
        }
        encoded_params = urllib.parse.urlencode(params) # encode parameters
        base_url = "https://quickstats.nass.usda.gov/api/api_GET/"
        full_url = f"{base_url}?{encoded_params}"
        data = self.fetch_api_data(full_url) # pull data from API
        
        self.add_data_to_file(data, 'state_data.json') # add unfilitered data to json file
        filtered_data = self.filter_data()
        self.add_data_to_file(filtered_data, 'crop_data.json') # add filtered data to json file
        self.convert_json_to_csv() # convert json file to csv file

    def fetch_api_data(self, url):
        response = requests.get(url)
        if response.status_code == 200: # successful request
            return response.json()
        else:
            response.raise_for_status() # raise exception if request fails
            
    def filter_data(self):
        filtered_data = []
        with open('state_data.json', 'r') as f: # open file of unfiltered json file 
            state_data = json.load(f)
        dict_list = state_data['data'] # list of dictionaries
        for item in dict_list: # loop through dictionaries
            if item.get("county_code") == "":
                new_item = {"State": item.get("state_alpha")}
                new_item["Amount"] = int(item.get("Value").replace(',', ''))
                # adds crop, state, and amount of acres of the crop planted per state to dictionary
                if len(item.get("state_alpha")) == 2 and item.get("state_alpha") != "US": # filter random entries and overall US data 
                    filtered_data.append(new_item)
        return filtered_data

    def add_data_to_file(self, data, filepath): # add filtered data to file
        with open(filepath, 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def convert_json_to_csv(self):
        with open('crop_data.json', 'r') as f:
            data = json.load(f)
        df = pd.DataFrame(data)
        df.to_csv('crop_data.csv', index=False)