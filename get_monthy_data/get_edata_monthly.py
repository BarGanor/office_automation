import pandas as pd
import requests

path= 'https://apis.cbs.gov.il/series/data/list?id=37615&format=json&download=false'
resp = requests.get(path)
print(resp.content.decode('utf-8'))
