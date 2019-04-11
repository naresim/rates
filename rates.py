import requests, json
#from pprint import pprint

date = input("Date: ")
if not date:
    date = latest

base = input("Currency: ")
rates = input("Exchange rates: ")

#result = requests.get('https://api.exchangeratesapi.io/latest?base=' + base )
link = 'https://api.exchangeratesapi.io/'
url = link + date + '?symbols=' + rates #+ '&base=' + base
result = requests.get( url=url , params={'base':base} )
output = result.json()
print(output)

