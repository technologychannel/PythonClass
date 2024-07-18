import requests
import json
url = "https://jsonguide.technologychannel.org/quotes.json"

f = requests.get(url)
quotes = json.loads(f.text)

for quote in quotes:
    print(quote['text'])
