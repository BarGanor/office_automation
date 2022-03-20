import requests
import pandas as pd
from datetime import datetime, date, timedelta


def cols_c_to_e_fdata():
    try:
        curr_year = date.today().year
        curr_month = date.today().month
        day = date.today().day
        df1 = pd.DataFrame()

        url_2019 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/mh-2019a/he/2019_mh.xlsx'
        url_2020 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/2020_mh/he/budget-execution_budget-execution-estimate_2020_mh.xlsx'
        url_2021 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/2021_mh/he/budget-execution_budget-execution-estimate_BudgetExecutionEstimate_BudgetDeficit_2021.xlsx'
        url_2022 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/data-for-2022/he/budget-execution_budget-execution-estimate_BudgetExecutionEstimate_BudgetDeficit_2022.xlsx'
        #         url_2023 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2023
        #         url_2024 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2024
        #         url_2025 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2025
        #         url_2026 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2026
        #         url_2027 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2027
        #         url_2028 = להוסיף פה את הכתובת אקסל הממתאים לשנת 2028

        for i in range(2019, curr_year + 1, 1):
            if i == 2019:
                url = url_2019
            elif i == 2020:
                url = url_2020
            elif i == 2021:
                url = url_2021
            elif i == 2022:
                url = url_2022
            # elif i == 2023:
            #     url = url_2023
            # elif i == 2024:
            #     url = url_2024
            # elif i == 2025:
            #     url = url_2025
            # elif i == 2026:
            #     url = url_2026
            # elif i == 2027:
            #     url = url_2027
            # elif i == 2028:
            #     url = url_2028

            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=0).dropna(how='all')
            df = df.loc[['עודף (+) / גירעון (-) למימון', 'עודף (+) / גירעון (-) ללא מתן אשראי נטו', 'סה"כ הכנסות']]
            today = date.today()
            col_names = []

            if i == curr_year:
                try:
                    df = df.iloc[:, 5:]
                    for month in range(1, curr_month, 1):
                        col_names.append(date(i, month, day).strftime('%m/%Y'))

                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
                except:
                    df = df.iloc[:, 4:]
                    for month in range(1, curr_month, 1):
                        col_names.append(date(i, month, day).strftime('%m/%Y'))

                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)

            else:
                try:
                    df = df.iloc[:, 4:-1]

                    df = df.dropna(how='all', axis=1)

                    for month1 in range(1, 13, 1):
                        col_names.append(date(i, month1, 1).strftime('%m/%Y'))
                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
                except:
                    df = df.iloc[:, 5:]

                    df = df.dropna(how='all', axis=1)

                    for month1 in range(1, 13, 1):
                        col_names.append(date(i, month1, 1).strftime('%m/%Y'))
                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
        return df1

    except Exception as e:
        print('problem getting col: C-E ' + str(e))


def cols_f_to_j_fdata():
    try:
        curr_year = date.today().year
        curr_month = date.today().month
        day = date.today().day
        df1 = pd.DataFrame()

        url_2021 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/2021_mh/he/budget-execution_budget-execution-estimate_BudgetExecutionEstimate_GovRevenue_2021.xlsx'
        url_2022 = 'https://www.gov.il/BlobFolder/dynamiccollectorresultitem/data-for-2022/he/budget-execution_budget-execution-estimate_BudgetExecutionEstimate_GovRevenue_2022.xlsx'
        #         url_2023 = להוסיף פה את הכתובת אקסל המתאים לשנת 2023
        #         url_2024 = להוסיף פה את הכתובת אקסל המתאים לשנת 2024
        #         url_2025 = להוסיף פה את הכתובת אקסל המתאים לשנת 2025
        #         url_2026 = להוסיף פה את הכתובת אקסל המתאים לשנת 2026
        #         url_2027 = להוסיף פה את הכתובת אקסל המתאים לשנת 2027
        #         url_2028 = להוסיף פה את הכתובת אקסל המתאים לשנת 2028

        for i in range(2021, curr_year + 1, 1):
            if i == 2021:
                url = url_2021
            elif i == 2022:
                url = url_2022
            # elif i == 2023:
            #     url = url_2023
            # elif i == 2024:
            #     url = url_2024
            # elif i == 2025:
            #     url = url_2025
            # elif i == 2026:
            #     url = url_2026
            # elif i == 2027:
            #     url = url_2027
            # elif i == 2028:
            #     url = url_2028

            resp = requests.get(url)
            df = pd.read_excel(resp.content, index_col=0).dropna(how='all')
            new_index = []
            for index in df.index:
                i = index.split()
                i = " ".join(i)
                new_index.append(i)
            df.index = new_index
            df = df.loc[
                ['סה"כ מסים ללא מע"מ יבוא ביטחוני', 'מסי הכנסה ורכוש', 'מכס ומע"מ ללא מע"מ יבוא ביטחוני', 'אגרות',
                 'מע"מ יבוא ביטחוני']]
            df = df.iloc[:, 5:].dropna(how='all', axis=1)
            col_names = []

            if i == curr_year:
                try:

                    for month in range(1, curr_month, 1):
                        col_names.append(date(curr_year, month, day).strftime('%m/%Y'))

                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
                except:
                    #                     df = df.iloc[:, 4:].dropna(how='all',axis=1)
                    for month in range(1, curr_month, 1):
                        col_names.append(date(curr_year, month, day).strftime('%m/%Y'))

                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)

            else:
                try:
                    #                     df = df.iloc[:, 4:-1].dropna(how='all',axis=1)

                    df = df.dropna(how='all', axis=1)

                    for month1 in range(1, 13, 1):
                        col_names.append(date(i, month1, 1).strftime('%m/%Y'))
                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
                except:
                    #                     df = df.iloc[:, 5:].dropna(how='all',axis=1)

                    df = df.dropna(how='all', axis=1)

                    for month1 in range(1, 13, 1):
                        col_names.append(date(i, month1, 1).strftime('%m/%Y'))
                    df.columns = col_names
                    df = df.transpose()
                    df1 = pd.concat([df1, df], axis=0)
        return df1

    except Exception as e:
        print('problem getting col: C-E ' + str(e))

