
import requests
import json

url = "https://jsonguide.technologychannel.org/person.json"

f = requests.get(url)
text = f.text
obj = json.loads(text)

print(obj["favourite_movies"][1])


# Display all quotes using number