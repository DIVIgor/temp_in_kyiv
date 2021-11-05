import requests as re
import os
import csv

from bs4 import BeautifulSoup


# URL = 'https://www.accuweather.com/en/ua/kyiv/324505/october-weather/324505?year2021'
HOST = 'https://www.accuweather.com/'
FILE = 'weather_kyiv_by_interval_2021.csv'
HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
MONTHS = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September','October', #'November', 'December'
    ]

# message with available months
print("Choose an interval to get the data (month num 1 - month num 2, 2021 year)")
print("Months:")
for id, month in enumerate(MONTHS, 1):
    print(id, month)

# get interval
month1 = int(input('Choose the start month of an interval: '))
month2 = int(input('Choose the final month of an interval: '))

months = MONTHS[month1-1:month2]

# creating a CSV file
def create_file(path, months):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Temperature in Kyiv'] + months)
        writer.writerow(['Day', 'Min temperature, °C', 'Max temperature, °C'])

# building urls for parsing
def build_urls(months):
    urls = []
    for m in months:
        urls.append(HOST + 'en/ua/kyiv/324505/' + m.lower() + '-weather/324505?year=2021')
    create_file(FILE, months)
    return urls
    
# getting an html page
def get_html(url, params=None):
    r = re.get(url, headers=HEADERS, params=params)
    return r

# collecting values
def get_values(html, month):
    soup = BeautifulSoup(html, 'html.parser')
    values = soup.find('div', class_='monthly-calendar').find_all('a')
    weather = []

    for val in values:
        if int(val.find('div', class_='date').get_text(strip=True)) == 1 and len(weather) > 0:
            break
        elif int(val.find('div', class_='date').get_text(strip=True)) > 1 and len(weather) == 0:
            continue
        else:
            weather.append({
                'day': val.find('div', class_='date').get_text(strip=True) + f' {month}',
                'min_t': val.find('div', class_='low').get_text(strip=True)[:-1],
                'max_t': val.find('div', class_='high').get_text(strip=True)[:-1]
            })
    return weather

# saving data
def save_file(vals, path):
    with open(path, 'a', newline='') as file:
        for val in vals:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([val['day'], val['min_t'], val['max_t']])

# parse function
def parse(url, month):
    html = get_html(url)
    if html.status_code == 200:
        weather = get_values(html.text, month)
    else:
        print('Error')
    save_file(weather, FILE)
    print(f'Get {len(weather)} temperature values')
    

# getting a list of URLs for chosen interval
urls = build_urls(months)

# parsing every URL
for url in urls:
    parse(url, months[urls.index(url)])

# run CSV
os.startfile(FILE)