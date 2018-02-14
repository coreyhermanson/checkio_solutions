# https://py.checkio.org/mission/the-most-frequent/

from collections import Counter


def most_frequent(data):
    c = Counter(data)
    return c.most_common(1)[0][0]
