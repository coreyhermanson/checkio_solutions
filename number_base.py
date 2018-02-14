# https://py.checkio.org/mission/number-radix/

# TODO: Understand this better


def number_base_checkio(str_number, radix):
    try:
        return int(str_number, radix)

    except ValueError:
        return -1


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    assert number_base_checkio("AF", 16) == 175, "Hex"
    assert number_base_checkio("101", 2) == 5, "Bin"
    assert number_base_checkio("101", 5) == 26, "5 base"
    assert number_base_checkio("Z", 36) == 35, "Z base"
    assert number_base_checkio("AB", 10) == -1, "B > A > 10"
