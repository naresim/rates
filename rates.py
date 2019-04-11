import requests, json
from pprint import pprint

base = input("Currency: ")
date = input("Date: ")
rates = input("Exchange rates: ")

#result = requests.get('https://api.exchangeratesapi.io/latest?base=' + base )
link = 'https://api.exchangeratesapi.io/'
url = link + 'history?start_at=' + date + '&end_at=' + date + '&symbols=' + rates + '&base=' + base
result = requests.get(url)
output = pprint(result.json())
print (output)

