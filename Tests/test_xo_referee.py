from xo_referee import check_3, check_rows_true, check_diag, check_columns_true, xoreferee_checkio

x_wins_col1 = [
    "X.O",
    "XX.",
    "XOO"]
o_wins_col2 = [
    "OO.",
    "XOX",
    "XOX"]
draw = [
    "OOX",
    "XXO",
    "OXX"]
x_wins_diag = [
    "O.X",
    "XX.",
    "XOO"]
o_wins_diag = [
    "O.X",
    "XO.",
    "XOO"]
o_wins_row = [
    "X.O",
    "OOO",
    "XOX"
]
x_wins_row = [
    "XXX",
    "O..",
    "XOX"
]
draw_one_x = [
    "...",
    ".X.",
    "..."]


def test_check3():
    assert check_3("XXX")
    assert check_3("OOO")
    assert not check_3("XOX")
    assert not check_3("OX.")


def test_check_rows_bool():
    assert not check_rows_true(x_wins_col1)[0]
    assert not check_rows_true(o_wins_col2)[0]
    assert not check_rows_true(draw)[0]
    assert not check_rows_true(x_wins_diag)[0]
    assert not check_rows_true(draw_one_x)[0]
    assert check_rows_true(x_wins_row)[0]
    assert check_rows_true(o_wins_row)[0]


def test_check_rows_letter():
    assert check_rows_true(x_wins_row)[1] == "X"
    assert check_rows_true(o_wins_row)[1] == "O"
    assert check_rows_true(draw)[1] == "O"


def test_check_columns_bool():
    assert check_columns_true(x_wins_col1)[0]
    assert check_columns_true(o_wins_col2)[0]
    assert not check_columns_true(draw)[0]
    assert not check_columns_true(x_wins_diag)[0]
    assert not check_columns_true(x_wins_row)[0]
    assert not check_columns_true(o_wins_row)[0]
    assert not check_columns_true(draw_one_x)[0]


def test_check_columns_letter():
    assert check_columns_true(x_wins_col1)[1] == "X"
    assert check_columns_true(o_wins_col2)[1] == "O"
    assert check_columns_true(draw)[1] == "X"


def test_check_diag_bool():
    assert check_diag(x_wins_diag)[0]
    assert check_diag(o_wins_diag)[0]
    assert not check_diag(x_wins_col1)[0]
    assert not check_diag(o_wins_col2)[0]
    assert not check_diag(draw)[0]
    assert not check_diag(x_wins_row)[0]
    assert not check_diag(o_wins_row)[0]
    assert not check_diag(draw_one_x)[0]


def test_check_diag_letter():
    assert check_diag(x_wins_diag)[1] == "X"
    assert check_diag(o_wins_diag)[1] == "O"
    assert check_diag(draw)[1] == "X"


def test_xoreferee_checkio():
    assert xoreferee_checkio(draw_one_x) == "D"
