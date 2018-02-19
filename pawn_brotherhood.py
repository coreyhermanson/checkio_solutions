# https://py.checkio.org/mission/pawn-brotherhood/


def get_coordinates(pawn: str) -> tuple:
    column = ord(pawn[0]) - 96
    row = int(pawn[1])
    coordinate = (row, column)
    return coordinate


def get_pawn_neighbors(pawn: tuple) -> tuple:
    try:
        left_front = (pawn[0] - 1, pawn[1] - 1)
    except IndexError:
        left_front = None
    try:
        right_front = (pawn[0] - 1, pawn[1] + 1)
    except IndexError:
        right_front = None
    try:
        left_back = (pawn[0] + 1, pawn[1] - 1)
    except IndexError:
        left_back = None
    try:
        right_back = (pawn[0] + 1, pawn[1] + 1)
    except IndexError:
        right_back = None

    return (left_front, right_front, left_back, right_back)


def check_pawn(neighbors: tuple, pawn_indexes: set) -> bool:
    pawn_is_safe = False
    # Get values for pawn neighbors

    lf = neighbors[0]
    rf = neighbors[1]

    if any([lf in pawn_indexes, rf in pawn_indexes]):
        pawn_is_safe = True

    return pawn_is_safe


def pawn_brotherhood_checkio(set_of_strings: set) -> int:
    """
     Input: Placed pawns coordinates as a set of strings.
     Output: The number of safe pawns as a integer.
    """
    # Get indexes of coordinates
    set_of_pawn_indexes = set()
    for pawn_string in set_of_strings:
        coordinate = get_coordinates(pawn_string)
        set_of_pawn_indexes.add(coordinate)

    # Check if pawns are safe
    safe_pawns = 0
    for pawn in set_of_pawn_indexes:
        neighbors = get_pawn_neighbors(pawn)
        if check_pawn(neighbors, set_of_pawn_indexes):
            safe_pawns += 1
        else:
            continue

    return safe_pawns


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert pawn_brotherhood_checkio({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert pawn_brotherhood_checkio({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
