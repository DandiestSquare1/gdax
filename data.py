import requests
from datetime import datetime, timedelta


def get_data(ticker, granularity):


    start = datetime.now() - timedelta(hours=24)
    end = datetime.now()

    start = start.isoformat()
    end = end.isoformat()

    url = 'https://api.gdax.com/products/{}-usd/candles?start={}&end={}&granularity={}'\
        .format(ticker, start, end, granularity)

    response = requests.get(url)
    data = response.json()

    count = 0

    for x in data:
        count += 1
        print(x)
    print(count)

get_data('eth', 300)