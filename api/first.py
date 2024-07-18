
import requests
import json

url = "https://jsonguide.technologychannel.org/info.json"

f = requests.get(url)
text = f.text
obj = json.loads(text)

print(obj["name"])