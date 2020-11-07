import requests
import json

# response = requests.get("https://api.nal.usda.gov/fdc/v1/foods/list?api_key=9GedmJalgsSJb0tBIPCsJj4TVTd1OQl6LA62ciQ9")

URL = "https://api.nal.usda.gov/fdc/v1/foods/list?"
API_KEY = "9GedmJalgsSJb0tBIPCsJj4TVTd1OQl6LA62ciQ9"
OK_STATUS = 200
# print(response.status_code)
# print(response.json())

def get_url_string(url, key):
    url_string = url
    if url[len(url) - 1] != '?':
        url_string += '?'
    url_string += "api_key=" + API_KEY
    return url_string

def json_text_formatter(json_response):
    return json.dumps(json_response, sort_keys=True, indent=4)

def json_text_to_array(json_text):
    # create a formatted string of the Python JSON object
    foods = json.loads(json_text)
    return foods

# json_file = response.json()
# json_file_formatted = json_text_formatter(json_file)

# for food in json_filter(json_file_formatted):
#     print(food.get('description'))

def api_handler():
    url_string = get_url_string(URL, API_KEY)
    food_array = []
    try:
        response = requests.get(url_string)
        if response.status_code == OK_STATUS:
            json_file = response.json()
            json_file_formatted = json_text_formatter(json_file)
            food_array = json_text_to_array(json_file_formatted)
    except Exception as e:
        print("Problem: {}".format(e))
    return food_array