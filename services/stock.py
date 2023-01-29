import requests
from datetime import datetime


def get_stock(symbol, interval="5min", range="1mo"):

    symbol = symbol.replace(" ", "").upper()
    interval = interval.replace(" ", "")

    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-chart"

    querystring = {"interval": interval, "symbol": symbol, "range": range, "region": "US", "includePrePost": "false",
                   "useYfid": "true", "includeAdjustedClose": "true", "events": "capitalGain,div,split"}

    headers = {
        "X-RapidAPI-Key": "0a9bd9ad36msh9da804e09688e05p1fcfcejsne6c5cc60e965",
        "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.json()['chart']['result'][0]


def fix_key(price_type_key): return ''.join(
    price_type_key.split(" ")[1:])


def get_time(res):
    timestamp = res['timestamp']
    datetimes = [datetime.fromtimestamp(time) for time in timestamp]

    return datetimes


def get_prices(res):
    return res['indicators']['quote'][0]


# res = get_stock("msft")

# times_data, prices_data = get_time_price(res)

# print(times_data)
# print()
# print(prices_data)
