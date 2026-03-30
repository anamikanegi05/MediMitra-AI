import json
from config import HOSPITAL_DATA_PATH

def get_nearby_hospital():
    try:
        with open(HOSPITAL_DATA_PATH, "r") as f:
            hospitals = json.load(f)

        # pick first hospital
        h = hospitals[0]
        return f"{h['name']} - {h['phone']}"

    except:
        return "Hospital data not available"
