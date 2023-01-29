import requests

url = "https://alpha-vantage.p.rapidapi.com/query"


def get_stock(symbol, interval="1min"):

    symbol = symbol.replace(" ", "").upper()
    interval = interval.replace(" ", "")

    print(symbol, interval)
    querystring = {"interval": interval, "function": "TIME_SERIES_INTRADAY",
                   "symbol": symbol, "datatype": "json", "output_size": "compact"}

    headers = {
        "X-RapidAPI-Key": "0a9bd9ad36msh9da804e09688e05p1fcfcejsne6c5cc60e965",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    # print(response.json()['Meta Data'])
    return response.json()


def fix_key(price_type_key): return ''.join(
    price_type_key.split(" ")[1:])


def get_time_price(res, interval="1min"):
    time_series = res['Time Series ' + '(' + interval + ')']
    times = list(time_series.keys())
    prices = list(time_series.values())

    formatted_prices = []
    for price in prices:
        formatted_price = {}
        for old_key in price.keys():
            formatted_price[fix_key(old_key)] = price[old_key]

        formatted_prices.append(formatted_price)

    return times, formatted_prices


# res = get_stock("msft")

# times_data, prices_data = get_time_price(res)

# print(times_data)
# print()
# print(prices_data)
