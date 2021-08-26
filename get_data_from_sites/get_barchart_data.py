# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import json
#
#
# def getBarChartData(index_name):
#     headers = {
#         'authority': 'www.barchart.com',
#         'method': 'GET',
#         'scheme': 'https',
#         'accept': 'application/json',
#         'cookie': '_gcl_au=1.1.1058381329.1626952365; _fbp=fb.1.1626952365592.499419369; _ga=GA1.2.81588553.1626952366; bcFreeUserPageView=0; __aaxsc=2; __gads=ID=45f23361e38ad57e:T=1626952370:S=ALNI_MbSZynn46fH_llcRYAlb5-XJVtrvw; '
#                   '__qca=P0-400029264-1626952371333; _admrla=2.0-bab00ad0-3ae4-c2e3-f697-cd0e9887c948; '
#                   'market=eyJpdiI6ImtPTHkxTFVKVGNITnlXS1F1WDE2U0E9PSIsInZhbHVlIjoidFFVUzEwdlJlRXQwUDRtcnVvVUNTUT09IiwibWFjIjoiNGU4ZGQ5ZDg0YWU3M2FiYmM3YmIwZGMxMTMzYTE0N2Y2NThlMTEwOTgzODQxOWQ2MTc1OTFkOTc2NzU2ZTJmYyJ9; sd-09012021PageView=1; '
#                   'sd-09012021WebinarClosed=true; _gid=GA1.2.449194142.1629966873; IC_ViewCounter_www.barchart.com=1; aasd=3%7C1629966875516; '
#                   '_awl=2.1629966881.0.4-ee3647f-bab00ad03ae4c2e3f697cd0e9887c948-6763652d6575726f70652d7765737431-6127521c-0; '
#                   'laravel_token'
#                   '=eyJpdiI6IndPYnM1VjdBUTg0MDhqSTVKM2NBRWc9PSIsInZhbHVlIjoiTmFoY1UwL3p0a2JxSloyblpGUVpVMHpUQnBKbXNIbmJxL3RBalZScmJ1T0JJM0lXT3RRd0hySDhJaFY0a3FRRk5MaVZDMWVFWFBLbE5qc1liTUtvREg2aEhaTTFvSHlOYW01dzRYYW81cHdRKzJ1WnJ0VjRRd3hKWm9TVVdQRWdhaFQyOGhrQzU5TUxWelNEck9ZeFdpeEc4R2VGRDhrRWVydWVCRGZpOEQ3WUovVnB0OUtnb3RNOExNRzU1aEdrZVlZc0h1M3FPYzZucXZRN0R5MFJQUkd3ZlUxMnJvYS9yQSt3WU5pbGJ0dmdRTi9lcEFIL1F5TUN3cDgrbVBYRyIsIm1hYyI6IjVhYjRmZDNmYmU3OTljMmM2ZmViNmUyNjQwNzQ5ZWE0OWYzYTkzYzIxYWQwYTJlNGZmNjllOWJmOWJkOTNjOWMifQ%3D%3D; XSRF-TOKEN=eyJpdiI6InVJM1pvaUswa0JxZEJZbzN0RVE0MUE9PSIsInZhbHVlIjoiWUNUV3h5TnMzVWZ0clRLY0l3WWp4WjVMNDNYdStJVENyRU9hTTU5cUhqL3NGQWxkQ3VVTm9FWXRlNTU4alE5VSIsIm1hYyI6ImM3NGU1YmExNjdhNTIwOTk1OGE1ZWQ1YzQ0MDU1ZmI3NzlkYmIyYzgxY2JiYWVjZmExOTVmNDBmZTAyMzAxYTEifQ%3D%3D; laravel_session=eyJpdiI6Im1NSmtmZWdrRjQ4S2VRbTVWK2MwcXc9PSIsInZhbHVlIjoiTDdHWkR5Nml3bm5YUXJBT0w3QnM3c3RwVTZmRGg5QURTbXRVZElTTXpDbGFJanpNL3dCV0lDZDlCWGtoaXVwcSIsIm1hYyI6IjdiOGYwOTNmNjA0NmMxOTFkMTJiOGI2YTM3YTdkMzhlZjc4NjNhYWNiYzQxOTE0NjMwZmVlMTExZTkwMzU0OWIifQ%3D%3D; _gat_UA-2009749-51=1',
#         'refer': 'https://www.barchart.com/futures/quotes/BWY00/price-history/historical?orderBy=tradeTime&orderDir=desc',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
#     }
#
#     if index_name == 'foodstuffs':
#         url = 'https://www.barchart.com/proxies/core-api/v1/historical/get?symbol=BWY00&fields=tradeTime.format(' \
#               'm%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield' \
#               '.description&raw=1 '
#         headers[
#             'path'] = '/proxies/core-api/v1/historical/get?symbol=BWY00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1'
#         headers[
#             'x-xsrf-token'] = 'eyJpdiI6InVJM1pvaUswa0JxZEJZbzN0RVE0MUE9PSIsInZhbHVlIjoiWUNUV3h5TnMzVWZ0clRLY0l3WWp4WjVMNDNYdStJVENyRU9hTTU5cUhqL3NGQWxkQ3VVTm9FWXRlNTU4alE5VSIsIm1hYyI6ImM3NGU1YmExNjdhNTIwOTk1OGE1ZWQ1YzQ0MDU1ZmI3NzlkYmIyYzgxY2JiYWVjZmExOTVmNDBmZTAyMzAxYTEifQ=='
#
#     elif index_name == 'industrials':
#         url = 'https://www.barchart.com/proxies/core-api/v1/historical/get?symbol=BVY00&fields=tradeTime.format(' \
#               'm%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield' \
#               '.description&raw=1 '
#
#         headers['path'] = '/proxies/core-api/v1/historical/get?symbol=BWY00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod' \
#                           '&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1 '
#         headers[
#             'x-xsrf-token'] = 'eyJpdiI6IkZmdnlPbWxaSG5vT3VnWmtWNlkvOWc9PSIsInZhbHVlIjoibUpaMkRXc0U4RDBZbkkvcllyMjJwa0UrSmxZY21VTzRLMy9zVFJvek0wYXh6alI0VnA5RG1KOXZFZ3VpT2FNNiIsIm1hYyI6ImY3MzQ4YjU3MTNhMmZkYTdmMDNhNTVhZGEzYjk2MDFhMmI0NTBkOTIzZDg3N2M1NmEwOTRhYTQ0M2FlMGMxMzQifQ== '
#
#     elif index_name == 'textiles':
#         url = 'https://www.barchart.com/proxies/core-api/v1/historical/get?symbol=BUY00&fields=tradeTime.format(' \
#               'm%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield' \
#               '.description&raw=1 '
#
#         headers[
#             'path'] = '/proxies/core-api/v1/historical/get?symbol=BUY00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1'
#         headers[
#             'x-xsrf-token'] = 'eyJpdiI6ImxKNE16bEZUQW12QXFLWlNFcHJXNEE9PSIsInZhbHVlIjoiN2VyUjkzOFByTW1ZRURHQ2FqYkE4cmphV3BLRW5aaERpalhvclF5S29mMk9IYWNBNnJGS2p5em93TnlXOVlDSiIsIm1hYyI6IjBlYTk1ZDBiMWMwYjUyZTEyYmIyNzY0YmI3YzIxOWJiNmZiZjQ5NjUxZjk2ZmE1MjI0OTRmMDU2NWM2ZjFkMTcifQ=='
#
#     elif index_name == 'metals':
#         url = 'https://www.barchart.com/proxies/core-api/v1/historical/get?symbol=B7Y00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1'
#         headers[
#             'path'] = '/proxies/core-api/v1/historical/get?symbol=BUY00&fields=tradeTime.format(m%2Fd%2FY)%2CopenPrice%2ChighPrice%2ClowPrice%2ClastPrice%2CpriceChange%2CpercentChange%2Cvolume%2CopenInterest%2CsymbolCode%2CsymbolType&type=eod&orderBy=tradeTime&orderDir=desc&limit=65&meta=field.shortName%2Cfield.type%2Cfield.description&raw=1'
#         headers[
#             'x-xsrf-token'] = 'eyJpdiI6IkppRVhLZjFJaUIwS25BNkZSMVhGb0E9PSIsInZhbHVlIjoidmhMbjNqVEl0OURtNERuRW0wZy9McGR0RFRuMDFlK3NxMVlNbUFLWEtkSS9kZDBTWmR4ZmdMRFdOd1BOOGw5MiIsIm1hYyI6IjNhMTc5ZGYxMTNjNDZiYTA1ZTcyMWVjZjA0ZjRmNjgzNDM1MmUzZWZjNTc0MGU5MjU5YzA5ZDk0YTk3MmMyMjkifQ=='
#
#     response = requests.get(url, headers=headers)
#     print(response.text)
#     # response_dct = json.loads(response)
#
#     # df = pd.DataFrame()
#     # for datum in response_dct.get('data'):
#     #     trade_time = datum.get('tradeTime')
#     #     last_price = datum.get('lastPrice')
#     #     temp = pd.DataFrame({'Date': [trade_time], index_name: [last_price]})
#     #     df = pd.concat([df, temp], axis=0, ignore_index=False)
#     #
#     # df['Date'] = pd.to_datetime(df['Date'])
#     # return df.set_index('Date')
# print(getBarChartData('metals'))