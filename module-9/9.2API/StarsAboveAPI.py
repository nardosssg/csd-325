# Create a program that includes the following:
# Find a simple API. I will be using the Stars Above API
# Test the connection to your API, output results. ##got 200 back
# Print out the response from the request, with no formatting. # came back in one straight line
# Print out the response with same formatting as the tutorial program.
# Run the program and take a screenshot of the results.


import requests
import json

response = requests.get('https://swapi.dev/api/planets/1/')
print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
