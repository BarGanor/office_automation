from flask import Flask, request, render_template, send_file
import pandas as pd
import numpy as np
import xlsxwriter
from datetime import datetime
import io

app: Flask = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/result', methods=['POST'])
def result():
    filename = request.files['file']
    price = float(request.form['price'])
    magnom = float(request.form['magnum_price'])
    mishtachim = float(request.form['mishtachim_price'])
    karton = float(request.form['karton_price'])
    maarach = float(request.form['maarach_price'])
    Yekev_name = request.form['winery']
    month = request.form['month']

    def recipt(filename, price, magnom, mishtachim, Yekev_name, karton, maarach, month):
        xlsx = pd.ExcelFile(filename)
        sheet_names = xlsx.sheet_names
        sheet_names = [sheet for sheet in sheet_names if '.' in sheet]
        df_dict = {}
        for i in sheet_names:
            try:
                df1 = pd.read_excel(filename, sheet_name=i, header=6)
                df1 = df1.dropna(axis=0, how='all')
                df1 = df1.dropna(axis=1, how='all')
                df1 = df1.iloc[:29]

                pivot_plats = df1.pivot_table(
                    index=['סוג יין', 'סוג\nקפסולות', 'סוג\nתויות', 'קרטון', 'בקבוק', 'מדבקת\nקרטון', "סטרץ'\nמכונה",
                           "מילוי\nאו\nמערך חוזר"],
                    values=['כמות \nבקבוקים\nבמשטח'], aggfunc=['sum', 'count'])

                df = pd.DataFrame(pivot_plats.to_records())

                # pivot_plats
                df.rename(columns={df.columns[1]: 'קפסולות', df.columns[2]: 'תויות', df.columns[3]: 'אריזה',
                                   df.columns[4]: 'סוג בקבוק', df.columns[5]: 'מדבקת קרטון',
                                   df.columns[6]: 'משטחים לחיוב', df.columns[7]: 'מילוי או מערך חוזר',
                                   df.columns[8]: 'כמות בקבוקים', df.columns[9]: 'מספר משטחים'}, inplace=True)
                df['לתשלום'] = np.where(df['סוג יין'].str.contains("מגנום"), df["כמות בקבוקים"] * magnom,
                                        df["כמות בקבוקים"] * price)
                df['יום'] = i
                cols = df.columns.tolist()
                cols = cols[-1:] + cols[:-1]
                df = df[cols]
                df_dict[i] = df
            except Exception:
                pass
        df = pd.concat(df_dict.values(), ignore_index=True)

        df.insert(1, "יקב", Yekev_name)

        ####
        rating = []
        for row, val in zip(df["מדבקת קרטון"], df["כמות בקבוקים"]):
            if row == "לחיוב":
                rating.append(val / 6)
            else:
                rating.append(0)
        df['מדבקת קרטון לחיוב'] = rating

        ###

        strech = []
        for row, val in zip(df["משטחים לחיוב"], df["מספר משטחים"]):
            if row == "לחיוב":
                strech.append(val)
            else:
                strech.append(0)
        df["משטחים סטרץ' לחיוב"] = strech
        ###

        df['לתשלום'] = np.where(
            (~df["מילוי או מערך חוזר"].str.contains("מילוי")) & (~df['סוג יין'].str.contains("מגנום")),
            df["כמות בקבוקים"] * maarach, df['לתשלום'])

        ###

        df['מילוי'] = np.where((df["מילוי או מערך חוזר"].str.contains("מילוי")), df["כמות בקבוקים"], 0)
        df['מערך חוזר'] = np.where((~df["מילוי או מערך חוזר"].str.contains("מילוי")), df["כמות בקבוקים"], 0)
        ###

        df['הערות'] = np.where((df["מילוי או מערך חוזר"].str.contains("מילוי")), "", "")
        ###
        df.loc['Total'] = df.sum(numeric_only=True, axis=0)

        df.loc['לתשלום הכללי', 'לתשלום'] = df.loc['Total', 'לתשלום']
        df.loc['לתשלום על המשטחים', 'לתשלום'] = df.loc['Total', "משטחים סטרץ' לחיוב"] * mishtachim
        df.loc['לתשלום הכללי', 'מערך חוזר'] = "ביקבוק"
        df.loc['לתשלום על המשטחים', 'מערך חוזר'] = "סטרץ' מכונה"
        df.loc['מדבקות קרטון', 'לתשלום'] = df.loc['Total', "מדבקת קרטון לחיוב"] * karton
        df.loc['מדבקות קרטון', 'מערך חוזר'] = 'מדבקות קרטון'
        df.loc['סה"כ לפני מע"מ', 'לתשלום'] = df.loc['לתשלום הכללי', 'לתשלום'] + df.loc['לתשלום על המשטחים', 'לתשלום'] + \
                                             df.loc['מדבקות קרטון', 'לתשלום']
        df.loc['סה"כ לפני מע"מ', 'מערך חוזר'] = 'סה"כ לפני מע"מ'
        df.loc['מע"מ 17%', 'מערך חוזר'] = 'מע"מ 17%'
        df.loc['מע"מ 17%', 'לתשלום'] = df.loc['סה"כ לפני מע"מ', 'לתשלום'] * 0.17
        df.loc['לתשלום עד:', 'מערך חוזר'] = "לתשלום עד:"
        df.loc['לתשלום עד:', 'לתשלום'] = df.loc['סה"כ לפני מע"מ', 'לתשלום'] + df.loc['מע"מ 17%', 'לתשלום']
        ###
        column_to_move = df.pop("כמות בקבוקים")
        column_to_move1 = df.pop("מילוי")
        column_to_move2 = df.pop("הערות")
        column_to_move3 = df.pop("מערך חוזר")
        column_to_move4 = df.pop("לתשלום")
        column_to_move5 = df.pop("מדבקת קרטון לחיוב")
        column_to_move6 = df.pop("משטחים סטרץ' לחיוב")
        df.insert(3, "כמות בקבוקים", column_to_move)
        df.insert(4, "מילוי", column_to_move1)
        df.insert(9, "הערות", column_to_move2)
        df.insert(10, "מערך חוזר", column_to_move3)
        df.insert(11, "לתשלום", column_to_move4)
        df.insert(12, "מדבקת קרטון לחיוב", column_to_move5)
        df.insert(13, "מדבקת סטרץ' לחיוב", column_to_move6)
        ###

        df['כמות יומית'] = np.where((df["מילוי או מערך חוזר"].str.contains("מילוי")), "", "")
        df['כמות מנות'] = np.where((df["מילוי או מערך חוזר"].str.contains("מילוי")), "", "")
        df['ספק מזון'] = np.where((df["מילוי או מערך חוזר"].str.contains("מילוי")), "", "")

        ###

        df = df.drop(columns=['מדבקת קרטון', 'משטחים לחיוב', 'מילוי או מערך חוזר', 'מספר משטחים', 'סוג בקבוק'])
        new_row = pd.DataFrame().reindex_like(df).iloc[:1]

        idx_pos = -6

        df = pd.concat([df.iloc[:idx_pos], new_row, df.iloc[idx_pos:]]).reset_index(drop=True)
        ##
        df.rename(columns={"מדבקת סטרץ' לחיוב": "משטחים"}, inplace=True)
        df.rename(columns={"מדבקת קרטון לחיוב": "מדבקת קרטון"}, inplace=True)
        ###
        output = io.BytesIO()

        writer = pd.ExcelWriter(f'{Yekev_name}.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name=f'{Yekev_name}', index=False, startrow=5)
        workbook = writer.book
        worksheet = writer.sheets[f'{Yekev_name}']

        # Define the formats
        cell_format1 = workbook.add_format({'num_format': '₪ #,##0'})
        cell_format2 = workbook.add_format({'num_format': '#,##0'})
        cell_format3 = workbook.add_format({'bold': True, 'font_color': 'red', 'num_format': '₪ #.##0'})
        cell_format4 = workbook.add_format({'bold': True})

        # Set the columns width and format
        worksheet.set_column('K:K', None, cell_format1)
        worksheet.set_column('E:E', None, cell_format2)
        worksheet.set_column('D:D', None, cell_format2)
        worksheet.set_column('L:L', None, cell_format1)

        if magnom > 0:
            worksheet.write('F4', "מגנום:", cell_format4)
            worksheet.write('E4', magnom, cell_format3)
        worksheet.write('F5', "רגיל:", cell_format4)
        worksheet.write('E5', price, cell_format3)
        worksheet.write('H1', f'ביקבוק יקב {Yekev_name}', cell_format4)
        worksheet.write('I2', 'חודש:', cell_format4)
        worksheet.write('H2', f'{month}', cell_format4)
        worksheet.write('G2', datetime.now().year, cell_format4)
        worksheet.write('D4', 'דוא"ל:', cell_format4)
        worksheet.write('D3', 'ח.פ', cell_format4)
        worksheet.write('D2', 'שם העסק:', cell_format4)

        worksheet.autofit()

        # Write the file
        writer.save()
        output.seek(0)
        return writer

    output = recipt(filename, price, magnom, mishtachim, Yekev_name, karton, maarach, month)  # modify this line
    return send_file(output)


if __name__ == '__main__':
    app.run(debug=True)
