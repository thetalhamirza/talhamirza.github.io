import requests
import sys

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

try:
    count = float(sys.argv[1])
    current = r.json()['bpi']['USD']['rate_float']
    amount = current * count
    print(f'${amount:,.4f}')

except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')


