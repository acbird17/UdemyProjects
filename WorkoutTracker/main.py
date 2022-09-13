import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

NUTRITION_ID = os.getenv("NUTRITION_ID")
NUTRITION_API_KEY = os.getenv("NUTRITION_KEY")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
TOKEN = os.getenv("AUTH_TOKEN")
GENDER = "Male"
WEIGHT_KG = 85
HEIGHT_CM = 183
AGE = 33

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercises did you do?:  ")

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    
    sheet_response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    
    print(sheet_response.text)