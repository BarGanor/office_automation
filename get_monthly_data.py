import requests
import pandas as pd

url = "/Heb/Statistics/StatRes/2021/Stat_202_l02_2021.xlsx"
r= requests.get(url, allow_redirects = True)
open('Stat_202_l02_2021.xlsx', 'wb').write(r.content)