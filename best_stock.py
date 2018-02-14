# https://py.checkio.org/mission/best-stock/


def best_stock(data):
    stock = max(data, key=lambda key: data[key])

    return stock

