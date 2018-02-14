# https://py.checkio.org/mission/index-power/


def index_power(array, n):
    """ Find Nth power of the element with index N """
    if n <= (len(array) - 1):
        return array[n] ** n

    else:
        return -1
