import requests
import pandas as pd

dls = "https://info.tase.co.il/Heb/Statistics/StatRes/2021/Stat_202_l02_2021.xlsx"
resp = requests.get(dls)
# print(resp.content)
print(pd.read_excel(resp.content))
