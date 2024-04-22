import requests
import pandas as pd
import io
import json
from tabulate import tabulate

cookie='_ga=GA1.1.565100908.1713423012; defaultLang=en; nsit=1KxBLMY1AgI-dsV4id9EQY6h; AKA_A2=A; _abck=28BFE1A0EE43BDF9EFC1B52842D2F691~0~YAAQO0w5F4DsCOKOAQAA231rBAsTv+MJk/lA06ep5JsIrdPra4gjeTF6rzps9NOB0d1fqUEZp8Pj/twxCstq0bmBA1snJovGHUb9wBAYWmOm5pLHhURL4sXCEHYHvg+43wG7JMAixrnPNAGR91ix5CJy1UWnKDCSI+kaKLIZ85wDBSiwFITZv1y16PfcchCvhfrEgMpJsu9nsdI3y9uIT25Uq+4N6rxzO26dV+3JFTZt6qFoEJvFcAp+S/3NK1BN/73g2hOZS+Zy6Haji4TWXze77GmAP/IYw8WQmcN60qgOGJEyct3YQGVx+9WF6FtfcQk5XiJ1MoAri7Gz3BtoBbqzaUCUvRsK8vtQtDrAm9a9eBMnQzJ1dw1hNXiRXq5tmne85yvPnbxJVPGhQ/WwUuUZY2DxO1bqX9o=~-1~-1~-1; _ga_QJZ4447QD3=GS1.1.1713766103.10.0.1713766103.0.0.0; ak_bmsc=8BCC5613E685E24B56942F5F794B1872~000000000000000000000000000000~YAAQO0w5F97tCOKOAQAAyoNrBBcue3tTHR13KJ2roYxGwwgTI50hv07F2aN6bNXnJ4/jMCs8+f4wiiM57wYXiTErUgbPti+uP2ik8LHvQUobeKdzyXVn4wvSTDTMJIkWQlNCp+IB2KQWbXH8LRynd08rwWNyL71GPGQg6jn78J5eGs/o2j7ItIVcmypD8fhudBJ6moCJr89ause+shNsFRCTmczQMQ7bf6cfJ3DhMY1JWuvIuP6uOn4HVAP4liVQ4tbx+yMD/YeT9qr0pwMG7a2qTDZoZOPIbR56BosyUqqqQ1Usb+dPB4wAon8xYKfadggs07s/tNEuz7ev/ImTWYS2MKaPgSj5SzAjrjKI6FX//9w/fY6+ppvCFkAvrtIyt3u3+it1XgiIlXdnzh4+m3VMGNrVgpwnYvCPWW7faP5eSFSl0cp6/zr2vPIfbye8MnXqtlh8P5QiBBx8C8Ai5Q==; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzc2NjEyMCwiZXhwIjoxNzEzNzczMzIwfQ.rY6cYzhsabD8NfoYocgeLwUTXcy2SkMtJZbowLt5jfM; bm_sz=6635571B72DD0875E2AB9FF27206838D~YAAQKkw5FzysfQGPAQAAzr1rBBfAOIUZJii5yD63fzJ6A19tvi+cwQ3UeAEMHAFGHdMBIDpPuMajje7SWx/L/G62yjs1bGcHI61pruMEKjCrnJ7tWcI7jVnMaDOG2BGnB5dWKo7gmjiMnIsLC8YEXrV+zCBNzTd0Ti78QNFxJVjanC8QntE6iYXGGLmEBFCKQUFp74cUOeOmdMJfzPWazbmuUKz0FUcZUM96a9/cGDl+8u2ZwF1bZ9X6xg5u7o5i6I2vYfmOyYNNkJVqXTYy5iB4I4wBTVNPmZtDZ5y3hH7YfOKF7U7Rn+83iW/IrE5+D6VbLYHe1N/stpZXe9wf1OlFN3kJzTpOdoTyfUL8FkWW0wwYP0zsr7Sv9iZu4fF9Dz4I5U7mUEW7ahF/gkUhYcGmC8XYFw==~4474179~3748912; RT="z=1&dm=nseindia.com&si=ab08845b-5b73-4583-a8a0-40e4f7478ff9&ss=lvak37k5&sl=0&se=8c&tt=0&bcn=%2F%2F684d0d4c.akstat.io%2F"; _ga_87M7PJ3R97=GS1.1.1713766102.13.1.1713766120.0.0.0; bm_sv=00D4949C47ABD15B6239B6A9CB1A1A49~YAAQKkw5F+usfQGPAQAAQsJrBBd6+Fmwwe4KkUyxwjdAwL6XsMx6rqIiWhh2YnGRdxIzJ2BOmNKOoN8WDYZxmljezi18i4D9pGwmmXYWAM07n4SaCBSdTLRzKvR04RAaU2CrwVh+AwX+kNAUdwh/yM/NB1I8rhehuMxqxVlANjAnEdtE21lUEIeUWcbl2fMUP4N9lXGZ6414jj+zqnpQ2rDtMBvDGpueP3xZYjlqNI7E6KtBCfzC6pDXDvuM0AiLTj4=~1'


stockurl = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
headers = {
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br, zstd',
'Accept-Language':'en-US,en-IN;q=0.9,en;q=0.8,bn;q=0.7',
'Cookie':cookie,
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
response = requests.get(url=stockurl , headers=headers )
# Parse the JSON response
data_dict = response.json()

# Extract the stock symbols and open prices as key-value pairs
stock_dict = {}
for stock in data_dict['data']:
    if stock['priority'] != 1:  # Exclude records with priority 1
        stock_dict[stock['symbol']] = {
            'open': stock['open'],
            'dayHigh': stock['dayHigh'],
            'dayLow': stock['dayLow'],
            'change': stock['change'],
            'pChange': stock['pChange']
        }
# print(stock_dict)
# Convert data into list of lists
table_data = []
for symbol, data in stock_dict.items():
    table_data.append([symbol, data['open'], data['dayHigh'], data['dayLow'], data['change'], data['pChange']])

# Print table
print(tabulate(table_data, headers=["Name", "Open price", "Day High", "Day Low", "Change", "P Change"]))

total_increase = 0
total_decrease = 0

for symbol, data in stock_dict.items():
    change = data['change']
    if change > 0:
        total_increase += change
    elif change < 0:
        total_decrease += abs(change)

# print('total_increase',total_increase)
# print('total_decrease',total_decrease)
if(total_increase):
    print("Profit:",total_increase-total_decrease)
else:
    print("Loss:",total_decrease-total_increase)

# working code don't  remove
# # Extract the stock names
# stock_dict = []
# for stock in data_dict['data']:
#     print("..........................................",stock)
#     symbol = stock['symbol']
#     open_price = stock['open']
    

#     # print(symbol)

# stock_dict = [{stock['symbol']: {'open': stock['open'], 'dayHigh': stock['dayHigh'], 'dayLow': stock['dayLow'], 'change': stock['change'], 'pChange': stock['pChange']}} for stock in data_dict['data']]
# # print(stock_dict)
# working code 