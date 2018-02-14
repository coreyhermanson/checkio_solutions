# https://py.checkio.org/mission/second-index/


def second_index(text: str, symbol: str):
    """ returns the second index of a symbol in a given text """

    first = text.find(symbol)
    second = text.find(symbol, first + 1)

    if second == -1:
        second = None

    return second
