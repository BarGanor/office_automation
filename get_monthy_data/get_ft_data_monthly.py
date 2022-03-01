import pandas as pd
import requests
from datetime import date


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

