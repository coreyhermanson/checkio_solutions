# https://py.checkio.org/mission/bigger-price/


def bigger_price(limit, data):
    prices = sorted(data, key=lambda k: k['price'], reverse=True)[:limit]

    return prices

