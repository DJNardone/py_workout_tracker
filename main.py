import requests
from datetime import datetime
import os

SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
APP_ID = os.environ.get("APP_ID")
APP_KEY = os.environ.get("APP_KEY")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"
}
sheety_headers = {
    "Authorization": SHEETY_AUTH
}

today = datetime.now()
formatted_date = today.strftime("%x")
formatted_time = today.strftime("%X")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_config = {
     "query": input("What was your workout today? "),
     "gender": "male",
     "weight_kg": 74.8,
     "height_cm": 176.00,
     "age": 50
}
exercise_response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()
duration = exercise_data['exercises'][0]['duration_min']
workout = exercise_data['exercises'][0]['name'].title()
calories = exercise_data['exercises'][0]['nf_calories']

sheety_endpoint = SHEETY_ENDPOINT
sheety_config = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": workout,
        "duration": duration,
        "calories": calories
    }
}
sheety_response = requests.post(url=sheety_endpoint, json=sheety_config, headers=sheety_headers)
sheety_response.raise_for_status()
print(sheety_response.text)

