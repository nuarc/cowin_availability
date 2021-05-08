import json
import time
from datetime import date

import pymsteams
import requests

today = date.today()
d1 = today.strftime("%d-%m-%Y")

district_ids = ["143", "146", "141"]  # north west delhi, north delhi, central delhi
webhook_url = "MS_TEAMS_WEB_HOOK_URL"


def check():
    available_centers = []
    for id in district_ids:
        query = {'date': d1, 'district_id': id}
        headers = {"User-Agent": "PostmanRuntime/7.26.10"}
        url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"

        print("query =", query)
        response = requests.get(url, params=query, headers=headers)
        centers = response.json()["centers"]
        for center in centers:
            name = center["name"]
            address = center["address"]
            pincode = center["pincode"]
            district_name = center["district_name"]

            for session in center["sessions"]:
                if session["min_age_limit"] == 18 and session["available_capacity"] > 0:
                    c = {'name': name, 'address': address, 'pincode': pincode, 'district_name': district_name,
                         "capacity": session["available_capacity"], "date": session["date"],
                         "vaccine": session["vaccine"]}
                    available_centers.append(c)
                    break
    if len(available_centers) > 0:
        print(available_centers)
        myTeamsMessage = pymsteams.connectorcard(webhook_url)
        myTeamsMessage.text(json.dumps(available_centers))
        myTeamsMessage.send()


while True:
    check()
    time.sleep(300)  # 5 mins
