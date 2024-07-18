import json
import requests


text = str(requests.get("https://jsonguide.technologychannel.org/info.json"))
                
obj = json.loads(text)
print(obj["name"])
print(obj["address"])