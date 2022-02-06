from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd

url = "https://yandex.ru/pogoda/chelyabinsk?from=tableau_yabro&lat=55.198826&lon=61.323891"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

div_temp_now = soup.find('div', class_='temp fact__temp fact__temp_size_s')
temp_now = div_temp_now.find('span', class_='temp__value temp__value_with-unit').text  # температура сейчас в челябинске
temp_hours = filter(lambda x: type(x) is type(1), map(lambda x: x.text, soup.find_all('div', class_='fact__hour-temp')))
print(*temp_hours)
sp = list(map(lambda x: x.text, soup.find_all('div', class_='fact__hour-temp')))
print(sp)

condition_now = soup.find('div', class_='link__condition day-anchor i-bem')
print(condition_now.text)

sp = map(lambda x: x.text, soup.find_all('div', class_='fact__hour-temp'))
sp = list(filter(lambda x: x != 'Восход' and x != 'Закат', sp))
del sp[0]
four_temps = (sp[::3])[:4]
print(four_temps)

wind_speed = soup.find('span', class_='wind-speed').text
print(wind_speed)

print(soup.find('div', class_='term term_orient_v fact__humidity').find('div', class_='term__value').text)