from pawn_brotherhood import pawn_brotherhood_checkio

set_1 = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}
set_2 = {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}


def test_pawn_brotherhood():
    assert pawn_brotherhood_checkio(set_1) == 6
    assert pawn_brotherhood_checkio(set_2) == 1
