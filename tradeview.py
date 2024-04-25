import requests
import pandas as pd
import io
import json
from tabulate import tabulate

cookie='_ga=GA1.1.565100908.1713423012; _abck=28BFE1A0EE43BDF9EFC1B52842D2F691~0~YAAQKkw5F80rOROPAQAA625bEwsDViPcRFRhJ7gZu/Rzpw94uka0krP4mD42TyUlEfwYU4KAT8wGdUGpyncASYNkZka/GWZ9093hwJjY1FzGvJdT3VW1Kt+9FMzsVAB6mdr6a4RE3nPjl5ysfmdJrLcZHRZvsYx6FfljaDGyrTOkL35TWYy8/3KUhsNneh3DZ9RBr7ayLlrzK3I5+5SE3r1KGdoS5XcqMVm4QXfgeBfyu+r9Ui6R1A/nNpMzANflZhlOLcX1C90H2hpacYJY6GXEf8+eFiUpDva1n0TYIIcwHuY/lG6yA8dkS1lwQnZqG7hZcXOVo+W6rfmmRnv05pMj2lUWbbOF5il7BKu+gQ644Q7JvRsH23uJXOBCjg6hbIIgVP9gplQfbndrvzVYwNhov5lFNOm+tso=~-1~-1~-1; defaultLang=en; nsit=qRsvRpqxoJ3iD9RcqGdwFUgZ; AKA_A2=A; bm_sz=637EDF3CFA46E5CE406B444C9A35E392~YAAQKkw5FzBneBOPAQAAbkwxFBcqkhdGTtXqgWaw7SM6jMuCrVoNRWYzxk1thfKnaRP2WhBXt+79XhqY8oL+50ex9shuvSfXcB4NRhHRfgd+sDx8L5EgjtcBsuMSGLZNZrj4uSksg/t3haoHmCOSGwd/ahC2hEOp6FYE9zFVTA7AdAcgdpvCoa7reQ1qPdUerGZ85JHSQLQreD9H7tBtRqxd0Q7THg8roZIHA/jj92DYMPwsxk/x+5VqLoqpI+yDwnU8exEztfbmqT/7s3nbAXA8a9pCTuIzj32bGuJKGX+fA0z3977N70uXdugSZN1t3XtYJjwVChVrmEMrQNNIipa/yQo5Uak83PwsxMos8vZNRi++wCgp7F2Yywnkco07stq4gkkgQw6Xu9CNs1yhjApQcFKuyesU2Kx+VtVo/hlClWVs6OA=~3490883~3618113; _ga_QJZ4447QD3=GS1.1.1714030727.14.0.1714030727.0.0.0; ak_bmsc=218FC5F713866554CA6F5802A754B03F~000000000000000000000000000000~YAAQKkw5F2VpeBOPAQAAnlIxFBd/Oa0ydNbZc94l3zvFH6p+trM1gEzs4APizljUpESgbzWyHYCGcMhKfS3ClGdmbHNtcFe50308ddOTdeQHxN5Lex6MeNM9lX2S+EUnC19GMebYNWSLLxUJgw4uoJpLAba+dTobT/KMgqRVe3wtnRnd8LTjKaKu4oIEUAbMijfTYNiqGWLSuJh8Dl7Ro6NLsmywidDeViOc95XjxulE6w+Cexu9iE46tr3bhKBFi2b/z7OYtEPyBoFaGpmbktdlp4dLPRO49FU/qrw6glR/ByTkn+tcYSJ4etBXVipbHOlv3wykw/Na+r/9G0m6Ehui74xyY1GqnaouJgHGujsRgFP71J4vEydDN/i3phHK5v2Iyk0cUVHK11PuOAgVuuleZuhB0r2VHOMMgzFH2eaoRbVfNTMxjHIhIKFWXsivQmV1PczD4v9DtFHfl5b9Gg==; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxNDAzMDc1MiwiZXhwIjoxNzE0MDM3OTUyfQ.l4HPsBMzDLYUDY3M7r7OITPlsMe4acEt2JoTnsyc6B0; RT="z=1&dm=nseindia.com&si=ab08845b-5b73-4583-a8a0-40e4f7478ff9&ss=lvexn0g4&sl=0&se=8c&tt=0&bcn=%2F%2F684d0d46.akstat.io%2F"; _ga_87M7PJ3R97=GS1.1.1714030727.23.1.1714030753.0.0.0; bm_sv=4F5C03EE2F1F41A1D5D342E62B51C260~YAAQKkw5F3yGeBOPAQAABbcxFBfe5IXBPIzeOZzKQZcKFh3KGFXYRRUO1XWXaEyCErfS2NXCG+RAbXeSTuynlxLrpdmP030TiG8a/6OrFHeBjeDyRroRSrNcqv1elDUfLm1Fk1FIXkjZfo+9YdVNghD8txcAZPEO6QfhGyfldMCR/YwDbnpcKtxR2CbUf3IDtzZMm4RK9vmrq6Q2QlwEJvf7TlzvQGA3c8jdMD7wv4uwJO0WA3hGe7rXqeX3EwaZ1fs=~1'



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
if(total_increase > total_decrease ):
    print("Profit:",total_increase-total_decrease)
else:
    print("Loss:  (----)",total_decrease-total_increase)

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