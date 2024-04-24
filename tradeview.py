import requests
import pandas as pd
import io
import json
from tabulate import tabulate

cookie='_ga=GA1.1.565100908.1713423012; _ga_QJZ4447QD3=GS1.1.1713865899.13.0.1713865899.0.0.0; nsit=Ao1UifyJSaBtBmqy3Q_X2xN8; AKA_A2=A; defaultLang=en; ak_bmsc=C4FB3278928FD367DC5054D7684E1C7F~000000000000000000000000000000~YAAQKkw5FzmsDwmPAQAAFUGJDxdrkAtnJw60p0z7a8oA8FMYnGAzw/OiLVtr23IcRSzfLVhchH6qEZi+WUXq1qqc8L1ByJ6rChpAwDxV50GYzV80ay3FrWXcM7oojirebpoUZJ2X0lv/dKxL01rWRXizRK7Cn0ceFO3UKX3Q97Ma3oYC1ckfavkcGd6A0IxxoYhrO0XIoJD8tFv/sSsisnFQ3EebRYsm9LDUje/NC+Z0vWsnXq2XtVOUXJg+9Htg+TaPzMt+cHG0ZED8mKwpE4WmCyj+BOlswUbD6t7K9kow/MbM3V+n0RXfOEEebLG7sLCJlkUwg/nrRgTpRzcW4bEw3spoDHHrLSmlaozy3yJI55lJhz16bK7/lJRL/DO7SEy8+iWxetmnUgSDZJP0hi+iig+tbmXRtsc0JZK4rH45DXZ8Jmcyw+HCK8T8P2ubEVtuyfv/i8OwnkJC2OPauQ==; _abck=28BFE1A0EE43BDF9EFC1B52842D2F691~-1~YAAQKkw5F0etDwmPAQAAMESJDws9GXdzzZ0ViJcZ3qcVHcxKC+Vzh9v1PBReKIWvTUpJuNf5D+P3sxNrVto1786rLKSsVF968sedWomBcKwJVoHAdT7KwS98E6j58J9vnZU7ZkyWwfRt0fyfqCWk4gpKd9UO5NH/rShIc5A4dMuUEosCjEBImxZg7iEKCy6bOR0N2F/lsUmNyCVsM1EYo1a2uMQl2QTWkjVBTFNxcwwUIFpF6O4URCU+JzjATCRURuNmyKLbWdL2B/MnhJWgs8BucDJpoEIdXqbQ90ugxz3Ah6q1+e4KH2Hgs9Djx3Q9h/OsGjKo7mvYIVkcmc8cDxOGUSy2w7gX9/5plAeBlyxLIaVlYq75vWej0do2fkFYcEOIlK3srEncFeAlL4D0oZwtkcaBxGdgg0Xf~-1~||1-pNVsjRdsTB-1500-10-1000-2||~-1; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzk1MjY1NiwiZXhwIjoxNzEzOTU5ODU2fQ.wKlkHB7_Y5MTW4IYwBg8bCwDqkzVVOjLTjaS861xy4A; bm_sz=2C3130752D954A21C9E7566FAB5AA026~YAAQKkw5F93dDwmPAQAACcSJDxfzoVRHVJmBPkZnM2pFQp7E+urNNMn5eg1y1Tx/jbkcEBVYEotUD4kFHM+zLUHcoYHVfpheULVBJflKJy8VdrpCDJ8miafW67GGQ6sjAoAcX9x0VnMe74eY0sQC7A7LRh/Xhwy7w9gGLL8HqzSv9W9ptxc/ps5yyBrF7nQofkZ+ZhmQtqe1d8jRYorUYs+to7PwOwQrWOUfSZooIbvcc69YTM3biIvv0rmwrX3qf2TC7NEjyN6m+9hNzODv/A0rOsY9V7aVs0/eUrzmyvCIfUIkzYvLY0Wjfr1Y4sMbaQswt726h5fH1jNAaBWPsU1ETVWVuxvgXYXKPNb7TuQqToL2xXTEV0TiUQK9Gd8F5mfqM1gBWqS42u3KV1n3UbGwQgQm~4473144~3683381; RT="sl=1&ss=lvdn4hfh&tt=2r6&z=1&dm=nseindia.com&si=ab08845b-5b73-4583-a8a0-40e4f7478ff9&se=8c&bcn=%2F%2F684d0d41.akstat.io%2F"; _ga_87M7PJ3R97=GS1.1.1713952602.19.1.1713952637.0.0.0; bm_sv=6A8261E32780F073EF83B1224CBFE274~YAAQKkw5F4bfDwmPAQAAlsiJDxe5JvIvKNBdb2Tfn6JKlZuLf5+uOx278qOjTliohe/XYUBd7EPAzlk18txaJ87z5a4b6Dp3nCcnMSlp386nGuxhCOWnUZUbPn5Rb12F1na2boUF5niI6v0e5ZOqmhZUR5oourx+4ohey/2pagFO64JnMYXCOkC8ApbRnIwBtY+qwmv2MRPOb3BtZwNW41E4v0vQUhcZWp1PjWJV1M9geVUaOs0DaG1/aaMuq/b5ZRg=~1'


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