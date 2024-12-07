# Nardos Gebremedhin
# Module 9.2 APIs
# Following the tutorial https://www.dataquest.io/blog/api-in-python/


import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.json())


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
