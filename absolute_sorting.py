# https://py.checkio.org/mission/absolute-sorting/


def absolute_sorting_checkio(numbers_array):
    abs_array = sorted(numbers_array, key=lambda x: abs(x))

    return abs_array
