import requests, json
from pprint import pprint
print("Currency: ")
base = input()

result = requests.get("https://api.exchangeratesapi.io/latest?base=" + base )
output = pprint(result.json())
print (output)

