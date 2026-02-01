from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='table')
th_name = soup.find('th').text.strip()
print(th_name)