from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find_all('table', class_ = 'wikitable sortable')[0]
th = table.find_all('th')
tr = table.find_all('tr')
# print("tr", tr)
# print("table:", table)

th_title = [i.text.strip() for i in th]

# pandas part
df = pd.DataFrame(columns=th_title)
# print(df)


for table_row in tr[1:]:  # Skip the header row
    table_data = table_row.find_all('td')
    # print(table_data)
    individual_row_data = [i.text.strip() for i in table_data]
    # print(individual_row_data)
    length_of_df = len(df)
    df.loc[length_of_df] = individual_row_data

print(df)

# df.to_csv(r'C:\Users\sc\OneDrive\Documents\python practice\scraping_data_csv_output\companies_by_revenue.csv', index=False)
