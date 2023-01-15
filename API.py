import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime
p_api = "RGAPI-f1e454a7-3441-4f70-9c3c-d573da5f7b54"
url = "https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/PLATINUM/"

#requests all userid from platinum rank into a list
def request_league(url):
    list = ['I','II','III','IV']
    summName = []
    for i in range(len(list)-1):
        response = requests.get(url + list[i]+ '?api_key=' + p_api)
        response = response.json()
        print(json.dumps(response))
        for v in response:
            summName.append(v['summonerName'])
            #print(v['summonerName'])
    return summName    

print(request_league(url))

