from pawn_brotherhood import pawn_brotherhood_checkio, get_pawn_neighbors, get_coordinates, check_pawn

set_1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
set_2 = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}
neighbors_c3 = ((2, 2), (2, 4), (4, 2), (4, 4),)
neighbors_b6 = ((5, 1), (5, 3), (7, 1), (7, 3),)
set_1_coords = set((get_coordinates(x) for x in set_1))
set_2_coords = set((get_coordinates(x) for x in set_2))


def test_get_coordinates():
    # row, column
    assert get_coordinates("b4") == (4, 2)
    assert get_coordinates("c3") == (3, 3)
    assert get_coordinates("g4") == (4, 7)


def test_get_pawn_neighbors():
    assert get_pawn_neighbors((4, 6)) == (
        (3, 5),
        (3, 7),
        (5, 5),
        (5, 7),
    )
    assert get_pawn_neighbors((3, 3)) == (
        (2, 2),
        (2, 4),
        (4, 2),
        (4, 4),
    )


def test_check_pawn():
    assert check_pawn(neighbors_c3, set_1_coords) is True
    assert check_pawn(neighbors_b6, set_1_coords) is False


def test_pawn_brotherhood():
    assert pawn_brotherhood_checkio(set_1) == 6
    assert pawn_brotherhood_checkio(set_2) == 1
