import requests
import pandas as pd
import io
import json
from tabulate import tabulate

cookie='_ga=GA1.1.565100908.1713423012; _ga_QJZ4447QD3=GS1.1.1713865899.13.0.1713865899.0.0.0; nsit=SDe0ehRKCUEmda2eL67kTloM; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcxNDAxNjcxMCwiZXhwIjoxNzE0MDIzOTEwfQ.Gqxn6cG3Lc3YqMi0BAFOHOOHd92zksW01pktDzBYcfE; AKA_A2=A; _abck=28BFE1A0EE43BDF9EFC1B52842D2F691~0~YAAQKkw5F80rOROPAQAA625bEwsDViPcRFRhJ7gZu/Rzpw94uka0krP4mD42TyUlEfwYU4KAT8wGdUGpyncASYNkZka/GWZ9093hwJjY1FzGvJdT3VW1Kt+9FMzsVAB6mdr6a4RE3nPjl5ysfmdJrLcZHRZvsYx6FfljaDGyrTOkL35TWYy8/3KUhsNneh3DZ9RBr7ayLlrzK3I5+5SE3r1KGdoS5XcqMVm4QXfgeBfyu+r9Ui6R1A/nNpMzANflZhlOLcX1C90H2hpacYJY6GXEf8+eFiUpDva1n0TYIIcwHuY/lG6yA8dkS1lwQnZqG7hZcXOVo+W6rfmmRnv05pMj2lUWbbOF5il7BKu+gQ644Q7JvRsH23uJXOBCjg6hbIIgVP9gplQfbndrvzVYwNhov5lFNOm+tso=~-1~-1~-1; bm_sz=84008084DA7E3872364D2B1DF717335D~YAAQKkw5F9ArOROPAQAA625bExdmEqRUIOyt/keA3aUB3fgt/bvqwthvBf3obrPalUEt6u9wP+l5+PmLQbXSjEwrJF8OjUH0YobAOr20vp713ePAJJXtlNSfHIe298t7Bs7ptcfhLPIh2ePKn3fhSgn0QydYY1AFuA8ju+DD2JerjstE8l98Bv9b8NnxDoR/3fH9cX66+gc0MUsP49uAhRP2hioEFQMdsE1UcJCPYKOVccvoTDxETPZ5vDxYGO5mvFJHt3q/7lkLhRa2o1zqylKoKaRNp8M1L4tU3Kr4iYPTY6UKa2SQxTywrn+HwkEU9viJ29KYfI3qSWK27oiZ5vuS3rzYGWN7u9Ye7WVN0OoRoBpNHwralvhgCJSA+AltGYEc8T45HmgST5pq1to=~4277552~3619123; defaultLang=en; RT="sl=0&ss=lvepakwf&tt=0&z=1&dm=nseindia.com&si=ab08845b-5b73-4583-a8a0-40e4f7478ff9&se=8c&bcn=%2F%2F684d0d44.akstat.io%2F"; ak_bmsc=6B77385AB027630C7C2B3895B5283671~000000000000000000000000000000~YAAQKkw5F+4tOROPAQAAgnpbExe6AgV5PY2i9kmX5BlIa0UTk5uo3tHZrF+NN49bd0RZA6yn+qDNu8/2XoL2W+iBsOhdUB6x0VtJfvQHM1LcZPXefatgy44RYJ2L7nfmdo4dXFBz0uh4slhAm7yUnhrPUoMS9w8YFAGg2iPcM9Z9lRD8nb4DHPk+2KndO6ui5B0GtfYNUTq8FykcmQWPJQz4zVk3PIUc/wFiCp1rzvd+jHcJIYg7h4/ecPIobgpsCBB9xasc3Jd73EGJlrm/PBRZuVBCRtTDLTvUHyF7HI2qzM3OVVsidpFC0gzUGt0ZciAzf2tj8KSiTCBrotwJwhgylkGHXAvWE4thnoOhENOA5yz8cpoIj73itNllcEEJG3Bd8Cm5tWNchkVTAIB+FbweAPW0dcPBvuPYZe0X8SLQEx39mL0ZB8JG2ZnOACfUTuWAfpCdsngobs0lATDR6w==; _ga_87M7PJ3R97=GS1.1.1714016713.22.1.1714016713.0.0.0; bm_sv=6E122004A0C57BC6A58444ED50CE99D7~YAAQKkw5FxQuOROPAQAANHtbExcSFUVXvaXhJC+rRRafLsVHbmj9Q3y8FCPg5bu83+F70uIoTioj6SO/tea6taYsIHfEHM0x6EA2rEf71J/J3QoTzgZzamdaMpaaTEmHZI5xkidxhxlSMja63q7IUt21T5mmQd1QbVLZobCLjlws7oHf3+vNmGMtKg3fw50vmhdsd4uzMQsFZ1jCs3K2HwcmATZbGZzbLZHSii1J97zJ0nspClpfmhSew2TmFSt6LdQ=~1'

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