import requests
import pandas as pd

url = ' https://www.barchart.com/proxies/core-api/v1/historical/get?symbol=BWY00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1'
g
barchart_response = requests.get(url)