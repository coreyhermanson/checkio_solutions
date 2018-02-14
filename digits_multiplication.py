# https://py.checkio.org/mission/digits-multiplication/
from functools import reduce


def digits_multiplication_checkio(num):
    num_list = [int(digit) for digit in str(num)]
    filtered_args = list(filter(lambda x: x != 0, num_list))
    counter = reduce(lambda x, y: x * y, filtered_args)

    return counter
