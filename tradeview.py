import requests
import pandas as pd
import io
import json
from tabulate import tabulate

cookie='_ga=GA1.1.565100908.1713423012; _ga_QJZ4447QD3=GS1.1.1713702186.8.0.1713702186.0.0.0; nsit=7P11v7k0tFCtT2c-dWDbN-s8; AKA_A2=A; _abck=28BFE1A0EE43BDF9EFC1B52842D2F691~0~YAAQKkw5F6Y5XwGPAQAAcDAxAwtNX06Sljn834tbO7p4v5ejF4fuC8NceTDa9rFssO6e9X8zL/I7DLu/b5/cL+2f0mEx4bgKPORJF2Hf/ESv2tLbNFbQ2hZgqFwPykRfDX9JjqAh5HhSDNl72dK4g9IDinI32aKpd8HcEYEppc9RPE/sCGLZKBlD/waI6BByymq9xV+Og/jJeHDhGOWwxzGi1+98VCj+YvQluA4Xp1+Ovsj635MYzyXPftHVQHfhrSh2SF0Lsi+ZMFxelFpEXUOFMlnA9FKKH+gS3i/cLHORg/PLf3aIAGnUEjV8Bb+mHFIJK0pnx0tQU4LFeV8rG3Y6Kb+Qx9m0zoKcQdsH699aiLzTwJ86ovxle/jTMMgjAZJjLKs58Vih5LfdXxOsfy2zUkf72+OAAmM=~-1~-1~-1; defaultLang=en; ak_bmsc=7020671AE220860FDF12CDF1D274BC0A~000000000000000000000000000000~YAAQKkw5F785XwGPAQAAPjUxAxdp6sxDi62ybXP2dX7kh+f7t3x4GmOE4uCnnh+oe2S7khuwgpzfUG9C0F5UXntx7B9mJp7qPEgG9Ri9u/XZhrGcJNMnz2t0VHaf0CXyRf0Zs5Z+U4iPP4Y6gYdwLIGfotPj3LRuh931VOv4NwVnOo5CmRRWSkWcN5H54eLK4Htf6nP5fogGr38ScAdmpUx8wuoJ4UHQfR3z/s7/Lr5Fs1I2QfZDQIS5YgtXzlSmPstc+KjFjKGk2Lxf1a6c8z8wuSfNWhp+LCY9H/L7q1ohFoejlff+7dMVmdrSpJyIl2cZkmK53ETfM2g+/TPZYf76IWx5P6+eTKlWWGNYbR+onxNvXrXGuBA1rDaY/aciOALE6IOLspp/KPQqaMSaRLGh+crZYEWSizqnKey/EC7DPiWVax/DPusyjxFcMS9vb7nraj4dxRDvooOvhcXdNA==; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxMzc0NTUzNiwiZXhwIjoxNzEzNzUyNzM2fQ.bCAVKSlufKg5W-UsO2TcQU4wRbCkch58G6UdeQ1E7jA; bm_sz=531379DD80CEF584E0B0D5E4C0164E15~YAAQKkw5F4o8XwGPAQAAgqQxAxec7UtF5xcWWII0K+pe1IOssGQg0LBDiKVVlYJwCHr81Qo1/c6gDwn/ZbZsNKgWtvkzHowIQQP2od5STmFyKXhuRIEtFijckIHEw/GRL15SNHohuRSkZfm4FRRUNoQyRZeyKxBKgN2LCuwQy8WFPnDj5eeq9150YtlO0nqER539PvvrqBOMXbtSNpAQRKslOyy8dko6eojb+ULQyFB9YLtqogSe6k6rrrmEoZqB5zD6+gEZx7vjkMhUjZEGMpIXeKDYSsShk9vOXfqIcsjvmExz9YsWDp808VVd4y/em5UERh2VwoAavAzdITMTP9X/sBqsk0UoxmFuEpta0DkoXRgzwt4LNnkdGLFCZRAnsI+shKORwzD6tikSunuH1Yyro/943A==~3682358~3618629; RT="z=1&dm=nseindia.com&si=ab08845b-5b73-4583-a8a0-40e4f7478ff9&ss=lva7tprj&sl=1&se=8c&tt=3tq&bcn=%2F%2F684d0d44.akstat.io%2F"; _ga_87M7PJ3R97=GS1.1.1713745505.11.1.1713745535.0.0.0; bm_sv=2E634066F150CFD6006D8D4C538911F3~YAAQKkw5F6k8XwGPAQAA6KgxAxfmfMUVqkmelG2lUzjTYjZ3Ul2IBsku1SSDJB7xflncmCkA4n3FIP9PrAV8Bs+TRkU3KMqDc4iESyNxe5zhTxGRb570XkGm0mOjq+h4Y4rTzfHFyv4wrEntyhB9VlLvWTik0xRSBNWZwR2PPr4VscSy4L1xY+H/wBpVTB4PRGNRDkFFSmg10GaPi+q5FTg5GXsHLsuYmbyEpxavWJivzCtGoKpWS3qh6cCapuQ3fBU=~1'


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