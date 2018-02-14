# https://py.checkio.org/mission/most-numbers/


def most_numbers_checkio(*args):
    if args:
        return float(max(args)) - float(min(args))
    else:
        return 0

