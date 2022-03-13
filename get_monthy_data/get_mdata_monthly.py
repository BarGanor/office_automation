import requests
import pandas as pd
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from dateutil.relativedelta import relativedelta
import string
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)


def col_i_mdata():
    try:
        url = f'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/shcf10_h.xls'
        resp = requests.get(url)
        col = pd.read_excel(resp.content,sheet_name='אינפלציה צפויה',header=6 ,index_col=2).dropna(how='all')
        df = col.loc[:,'ציפיות משוק ההון1 לשנה הראשונה\n']
        df.name = 'ציפיות לאינפלציה משוק ההון (שנה קדימה)'
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')

        return df
    except Exception as e:
        print('problem getting cols: I: ' +str(e))


def col_j_mdata():
    try:
        url = f'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=FEDFUNDS&scale=left&cosd=1954-07-01&coed=2022-02-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-03-13&revision_date=2022-03-13&nd=1954-07-01'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=0)
        df = df.loc['observation_date':, :].iloc[1:, :]
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        df.columns = ['ריבית ארה"ב']

        return df
    except Exception as e:
        print('problem getting cols: J: ' +str(e))


def col_at_and_av_mdata():
    try:
        url = f'https://www.boi.org.il/he/DataAndStatistics/Lists/BoiTablesAndGraphs/heb_a5.xls'
        resp = requests.get(url)
        df = pd.read_excel(resp.content, index_col=0)
        df = df.loc['ממוצע חודשי של נתונים יומיים':'העליה או הירידה (-) במשך התקופה',:].iloc[1:-1,3:5].dropna(how='all')
        df.index = pd.to_datetime(df.index).strftime('%m/%Y')
        df.columns = ['M1 מקורי','M1 מנוכה']

        return df
    except Exception as e:
        print('problem getting cols: AT,AV: ' +str(e))


