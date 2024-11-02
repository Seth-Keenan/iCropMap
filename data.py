import requests
import json
from config import API_KEY

def fetch_api_data(url, params):
    params['key'] = API_KEY
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("FAILED")
        response.raise_for_status()

params = {
    'commodity_desc': 'CORN',
    'year__GE': '2024',
    'state_alpha': 'VA',
    'format': 'json'
}


url = "https://quickstats.nass.usda.gov/api/api_GET/"
data = fetch_api_data(url, params)

with open('crop_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data fetched and saved to crop_data.json")