# https://py.checkio.org/mission/all-the-same/


def all_the_same(elements: list) -> bool:
    is_all_equal = len(set(elements)) <= 1
    return is_all_equal
