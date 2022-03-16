import pandas as pd
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup


#פונקציות נצרכות לפונקציות הבאות
def get_message_number_exports(year,monthName):
    curr_year = date.today().year
    curr_month = date.today().month
    two_months_ago_name = (datetime.today() + relativedelta(months=-2)).strftime("%B")

    if monthName in ['December','November']:
        url = f'https://www.cbs.gov.il/en/mediarelease/Pages/{curr_year}/Exports-of-Services-{monthName}-{year}.aspx'
    else:
        url = f'https://www.cbs.gov.il/en/mediarelease/Pages/{year}/Exports-of-Services-{monthName}-{year}.aspx'

    resp = requests.get(url)
    soup = BeautifulSoup(resp.content.decode('utf-8'), features='lxml')
    tags = soup.find(class_="articleDetails")
    br_tags = tags.text.strip().split()
    message_number = br_tags[3].split("/")[0]
    return message_number

def get_curr_year_list_2_digit(year):
    curr_year = date.today().year
    list_of_numbers = list(str(year))
    curr_year_list_2_digit = list_of_numbers[2] + list_of_numbers[3]
    return curr_year_list_2_digit

def get_roman_number(number):
    roman_month = {1: 'I',2:'II',3:'III' ,4:'IV' ,5:'V' ,6:'VI' ,7:'VII' ,8:'VIII' ,9:'IX' ,10:'X' ,11:'XI' ,12:'XII'}
    return roman_month.get(number)


def get_key_by_value(roman_number):
    roman_month = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                   6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11:'XI',
                   12 :'XII'}
    return [name for name, age in roman_month.items() if age == roman_number][0]

######


def cols_c_to_bi_rdata():
    try:
        series_id = {'col_c': '624440', 'col_d': '79', 'col_e': '624477', 'col_f': '17', 'col_g': '78',
                     'col_h': '51317',
                     'col_j': '51315', 'col_k': '51306', 'col_l': '51316', 'col_m': '51305', 'col_n': '51314',
                     'col_o': '51285', 'col_p': '99', 'col_q': '82', 'col_r': '81', 'col_s': '51297', 'col_t': '51298',
                     'col_w': '624426', 'col_x': '624355', 'col_ab': '624429',
                     'col_ac': '624427', 'col_ad': '624430', 'col_af': '624407',
                     'col_ah': '624431', 'col_ai': '624432', 'col_ak': '624433', 'col_al': '624343', 'col_an': '624351',
                     'col_ao': '624324', 'col_ap': '624417', 'col_aq': '624419', 'col_ar': '624418',
                     'col_as': '624416', 'col_ay': '11207', 'col_az': '11200', 'col_bb': '11211', 'col_bc': '13621',
                     'col_be': '11209', 'col_bf': '11202',
                     'col_bh': '11212', 'col_bi': '221709'}

        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['exports_seasonal adjusted', 'imports_seasonal adjusted', 'trade balance_seasonal adjusted',
                      'exports_original', 'imports_original', 'יבוא מוצרי צריכה (סך כולל)', 'מזה: סהכ לצריכה שוטפת',
                      'מזה: סהכ מוצרים בני-קיימא', 'יבוא מוצרי צריכה מקורי', 'יבוא מוצרי צריכה בני קיימא מקורי',
                      'יבוא מוצרי צריכה שוטפת מקורי',
                      'סהכ יבוא חומרי גלם', 'יבוא חומרי גלם ללא יהלומים ודלק- מנוכה', 'דלק', 'יהלומים ברוטו',
                      'סהכ יבוא מוצרי השקעה ללא אוניות ומטוסים',
                      'סהכ יבוא מוצרי השקעה ללא אוניות ומטוסים- מנוכה עונתיות',
                      'תעשייה וחרושת, כרייה וחציבה ללא יהלומים מעובדים- מנוכה עונתיות',
                      'תעשייה וחרושת, כרייה וחציבה ללא יהלומים מעובדים- מקוריים', 'ייצור מוצרי מזון ומשקאות ומוצרי טבק',
                      'טקסטיל הלבשה ועור',
                      'עץ ריהוט נייר ודפוס', 'גומי ופלסטיק',
                      'ייצור מוצרי מתכת בהרכבה, מכונות וציוד לנמ"א וציוד חשמל ביתיים',
                      'ייצור מחשבים, מיכשור אלקטרוני ואופטי וציוד רפואי, דנטלי ואורטופדי',
                      'ייצור ציוד חשמלי ללא מכשירי חשמל בייתים',
                      'כלי הובלה', 'כלי נגינה, ספורט, צעצועים ומוצרים לנמ"א', 'עיבוד יהלומים (ברוטו)',
                      'תעשיות טכנולוגיה מסורתית', 'תעשיות טכנולוגיה מעורבת מסורתית',
                      'תעשיות טכנולוגיה מעורבת עילית',
                      'תעשיות טכנולוגיה עילית', 'ארה"ב מנוכה עונתיות', 'ארה"ב מקורי', 'האיחוד האירופי מנוכה עונתיות',
                      'האיחוד האירופי מקורי', 'אסיה מנוכה עונתיות',
                      'אסיה מקורי',
                      'אחרים לא כולל אסיה - מנוכה עונתיות', 'אחרים לא כולל אסיה - מקורי']
        return df
    except Exception as e:
        print('problem getting col: C-BI ' + str(e))


def col_bp_ce_ftdata():
    try:
        curr_year = date.today().year

        curr_month = date.today().month
        two_months_ago = (datetime.today() + relativedelta(months=-3)).month
        two_months_ago_name = (datetime.today() + relativedelta(months=-3)).strftime("%B")
        if two_months_ago_name in ['December', 'November']:
            url = f'https://www.cbs.gov.il/he/mediarelease/doclib/{curr_year}/{get_message_number_exports(curr_year - 1, two_months_ago_name)}/09_{get_curr_year_list_2_digit(curr_year)}_{get_message_number_exports(curr_year - 1, two_months_ago_name)}t1.xlsx'
            resp = requests.get(url)
            df = pd.read_excel(resp.content,header=5).dropna(how='all', axis=1).dropna(how='all', axis=0)
            df['Year'] = df['Year'].ffill()
            df = df.dropna(how='any', axis=0)
            df = df.bfill(axis=1)
            df['date'] = df['Month'].map(str) + '/' + df['Year'].map(str)
            df.index = df['date']
            index_col = []
            for i in df.index:
                d = i.split("/")
                if d[1].isnumeric():
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
                else:
                    d[1] = d[1].replace('*', "")
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
            df.index = index_col
            df = df.iloc[:,[3,10,22,25,18,2,9,21,24,17,4,5]]
            df.columns = ['סה"כ יצוא שירותים- מנוכה','יצוא שירותים עסקיים (לא כולל חברות הזנק)','שירותי תחבורה 1 - מנוכה','שירותי תחבורה 2 - מנוכה','יצוא שירותי תיירות - מנוכה','סה"כ יצוא שירותים - מקורי','יצוא שירותים עסקיים (לא כולל חברות הזנק) - מקורי','שירותי תחבורה (1) - מקורי','שירותי תחבורה (2) - מקורי','יצוא שירותי תיירות - מקורי','סה"כ ללא חברות הזנק - מקורי','סה"כ ללא חברות הזנק - מנוכה']
            return df
        else:
            url = f'https://www.cbs.gov.il/he/mediarelease/doclib/{curr_year}/{get_message_number_exports(curr_year - 1, two_months_ago_name)}/09_{get_curr_year_list_2_digit(curr_year)}_{get_message_number_exports(curr_year - 1, two_months_ago_name)}t1.xlsx'
            resp = requests.get(url)
            df = pd.read_excel(resp.content,header=5).dropna(how='all', axis=1).dropna(how='all', axis=0)
            df['Year'] = df['Year'].ffill()
            df = df.dropna(how='any', axis=0)
            df = df.bfill(axis=1)
            df['date'] = df['Month'].map(str) + '/' + df['Year'].map(str)
            df.index = df['date']
            index_col = []
            for i in df.index:
                d = i.split("/")
                if d[1].isnumeric():
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
                else:
                    d[1] = d[1].replace('*', "")
                    e = d[0].replace(d[0], str(get_key_by_value(d[0])))
                    r = e + "/" + d[1]
                    index_col.append(r)
            df.index = index_col
            df = df.iloc[:,[3,10,22,25,18,2,9,21,24,17,4,5]]
            df.columns = ['סה"כ יצוא שירותים- מנוכה','יצוא שירותים עסקיים (לא כולל חברות הזנק)','שירותי תחבורה 1 - מנוכה','שירותי תחבורה 2 - מנוכה','יצוא שירותי תיירות - מנוכה','סה"כ יצוא שירותים - מקורי','יצוא שירותים עסקיים (לא כולל חברות הזנק) - מקורי','שירותי תחבורה (1) - מקורי','שירותי תחבורה (2) - מקורי','יצוא שירותי תיירות - מקורי','סה"כ ללא חברות הזנק - מקורי','סה"כ ללא חברות הזנק - מנוכה']
            return df
    except Exception as e:
        print('problem getting cols: BP-CE ' + str(e))


def col_cb_ftdata():
    try:
        today = date.today()
        year = today.year
        try:
            url = f'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DPCERA3M086SBEA&scale=left&cosd=1959-01-01&coed=2222-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-03-01&revision_date=2099-01-01&nd=1959-01-01'
            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=0)
            df = df.iloc[24:, :]
            df.index = pd.to_datetime(df.index)
            df.index = df.index.strftime('%m/%Y')

            return df

        except:
            url = f'https://fred.stlouisfed.org/graph/fredgraph.xls?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=DPCERA3M086SBEA&scale=left&cosd=1959-01-01&coed={year - 1}-11-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2022-03-01&revision_date=2022-03-01&nd=1959-01-01'
            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=0)
            df = df.iloc[24:, :]
            df.index = pd.to_datetime(df.index)
            df.index = df.index.strftime('%m/%Y')

            return df
    except Exception as e:
        print('problem getting col: CB ' + str(e))


def col_dg_ftdata():
    try:
        today = date.today()
        three_month_ago = (today + relativedelta(months=-3))
        year = today.year
        month = today.month
        three_month_ago_name = three_month_ago.strftime("%B")
        if month >= 4:
            url = f'https://www.cpb.nl/sites/default/files/omnidownload/CPB-World-Trade-Monitor-{three_month_ago_name}-{year}.xlsx'
            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=1, header=3).transpose()
            df = df.loc[:,"World trade"].dropna(axis=0, how='any').iloc[1:,0]
            df.index = pd.to_datetime(df.index, format = '%YM%m')
            df = df.sort_index()
            df.index = df.index.strftime('%m/%Y')

            return df
        else:
            url = f'https://www.cpb.nl/sites/default/files/omnidownload/CPB-World-Trade-Monitor-{three_month_ago_name}-{year-1}.xlsx'
            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=1, header=3).transpose()
            df = df.loc[:,"World trade"].dropna(axis=0, how='any').iloc[1:,0]
            df.index = pd.to_datetime(df.index, format = '%YM%m')
            df = df.sort_index()
            df.index = df.index.strftime('%m/%Y')
            return df
    except Exception as e:
        print('problem getting col: DG ' + str(e))


def cols_dh_to_ev_ftdata():
    try:
        series_id = {'col_dh': '624356', 'col_di': '624425', 'col_dj': '624355',
                     'col_dk': '624426', 'col_dl': '624350',
                     'col_dn': '624324',
                     'col_do': '624412', 'col_dp': '624354',
                     'col_dq': '624428', 'col_dr': '624175', 'col_ds': '624406', 'col_dt': '624345',
                     'col_du': '624432', 'col_dv': '624233', 'col_dw': '624410', 'col_dx': '624343',
                     'col_dy': '624434', 'col_dz': '624158',
                     'col_ea': '624405', 'col_eb': '624344', 'col_ec': '624433', 'col_ed': '624346',
                     'col_ee': '624431', 'col_ef': '624153', 'col_eh': '624178',
                     'col_ei': '624407', 'col_ej': '624196',
                     'col_ek': '624408', 'col_el': '624209',
                     'col_en': '624349', 'col_eo': '624429', 'col_ep': '624348',
                     'col_eq': '624427', 'col_er': '624311', 'col_et': '624347',
                     'col_eu': '624430', 'col_ev': '624351'}
        df = pd.DataFrame()
        for id in series_id.keys():
            url = f'https://apis.cbs.gov.il/series/data/list?id={series_id.get(id)}&format=json&download=false'
            resp = requests.get(url).json()
            data = resp['DataSet']['Series'][0]['obs']
            col = pd.DataFrame.from_records(data)
            col = col.set_index('TimePeriod')
            col.index = pd.to_datetime(col.index)
            col = col.sort_index()
            col.index = col.index.strftime('%m/%Y')
            df = pd.concat([df, col], axis=1)
        df.columns = ['תעשייה, כרייה וחציבה - מקורי', 'תעשייה, כרייה וחציבה - מנוכה','תעשייה, כרייה וחציבה ללא יהלומים מעובדים - מקורי',
                      'תעשייה, כרייה וחציבה ללא יהלומים מעובדים - מנוכה', 'כרייה וחציבה - מקורי',
                     'עיבוד יהלומים - מקורי',
                     'עיבוד יהלומים - מנוכה', 'תעשייה ללא יהלומים - מקורי',
                     'תעשייה ללא יהלומים - מנוכה', 'תרופות - מקורי',
                      'תרופות - מנוכה', 'מחשבים וציוד אלקטרוני וציוד רפואי - מקורי',
                     'מחשבים וציוד אלקטרוני וציוד רפואי - מנוכה', 'מתוך זה - רכיבים אלקטרוניים - מקורי',
                      'מתוך זה - רכיבים אלקטרוניים - מנוכה', 'יצור כלי תחבורה והובלה - מקורי',
                     'יצור כלי תחבורה והובלה - מנוכה', 'כימיקלים ומוצריהם - מקורי',
                     'כימיקלים ומוצריהם - מנוכה', 'ציוד חשמלי - מקורי',
                      'ציוד חשמלי - מנוכה', 'מוצרי מתכת, מכונות וציוד - מקורי',
                     'מוצרי מתכת, מכונות וציוד - מנוכה', 'ייצור מוצרי נפט מזוקק - מקורי',
                      'מוצרי גומי ופלסטיק - מקורי',
                     'מוצרי גומי ופלסטיק - מנוכה', 'מוצרים על בסיס מינרלים אל מתכתיים - מקורי',
                     'מוצרים על בסיס מינרלים אל מתכתיים - מנוכה', 'מתכות בסיסיות - מקורי',
                     'מזון משקאות וטבק - מקורי', 'מזון משקאות וטבק - מנוכה',
                      'טקסטיל, הלבשה, הנעלה ומוצרי עור - מקורי',
                     'טקסטיל, הלבשה, הנעלה ומוצרי עור - מנוכה', 'תכשיטים - מקורי',
                      'מוצרי עץ, שעם וקש - מקורי',
                     'מוצרי עץ, שעם וקש - מנוכה', 'כלי נגינה משחקים וציוד ספורט - מקורי']
        return df
    except Exception as e:
        print('problem getting col: X-BA ' + str(e))

