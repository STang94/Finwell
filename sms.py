import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()
servicePlanId = getenv("SERVICEPLANID")
apiToken = getenv("APITOKEN")
sinchNumber = getenv("SINCHNUMBER")
toNumber = getenv("TONUMBER")
def send_sms(body:str):
    url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

    payload = {
    "from": sinchNumber,
    "to": [
        toNumber
    ],
    "body": body
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + apiToken
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
