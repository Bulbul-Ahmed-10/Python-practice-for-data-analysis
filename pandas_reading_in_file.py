import pandas as pd

# Reading a CSV file

_df_countries_data = pd.read_csv(r"D:\data-analysis-practice\python practice\pandas practice\countries_of_the_world.csv")
# print(_df_countries_data)

# Reading a JSON file
_df_countries_and_territories = pd.read_json(r"D:\data-analysis-practice\python practice\pandas practice\countries_and_terrotories.json")
# print(_df_countries_and_territories)

# Reading an Excel file
_df_excel_data = pd.read_excel(r"D:\data-analysis-practice\python practice\pandas practice\PracticeData.xlsx")
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# print(_df_excel_data)
# print(_df_excel_data.info())
# print(_df_excel_data.shape)
# print(_df_excel_data.head(10))
# print(_df_excel_data.tail(10))
# print(_df_excel_data.describe())
# print(_df_excel_data["Product"])
print(_df_excel_data.loc[482])