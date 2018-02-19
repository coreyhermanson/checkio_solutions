# https://py.checkio.org/mission/long-repeat/

from itertools import groupby


def long_repeat(line: str) -> int:
    groups = groupby(line)
    result_tuple_list = [(label, sum(1 for _ in group)) for label, group in groups]
    sorted_list = sorted(result_tuple_list, key=lambda tup: tup[1], reverse=True)
    try:
        longest_substring = sorted_list[0][1]
    except IndexError:
        longest_substring = 0

    return longest_substring


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('') == 0, "Zero"
    print('"Run" is good. How is "Check"?')
