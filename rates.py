import requests

date = input("Date: ")
if not date:
    date = 'latest'
    print('Setting date to current (latest) date.')

base = input("Currency: ")
rates = input("Exchange rates: ")

link = 'https://api.exchangeratesapi.io/'
url = link + date + '?symbols=' + rates
# + '&base=' + base
result = requests.get(url=url, params={'base': base})
output = result.json()

##rates=rates.split(", ") for future use

print("\n\nDate:%s\nCurrency:%s\nRates:%s"
      %(output['date'],output['base'],output['rates']))