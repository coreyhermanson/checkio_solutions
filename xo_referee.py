# https://py.checkio.org/mission/x-o-referee/


def check_3(text: str) -> bool:
    is_all_equal = (text == (len(text) * text[0]))
    if text[0] == ".":
        is_all_equal = False
    return is_all_equal


def check_rows_true(arr: list) -> tuple:
    equality_check = False
    for row in arr:
        letter = row[0]
        equality_check = check_3(row)
        if equality_check:
            break

    return (equality_check, letter)


def check_columns_true(arr: list) -> tuple:
    rows = list(zip(arr[0], arr[1], arr[2]))
    equality_check = False
    for row in rows:
        text = ''.join(row)
        letter = text[0]
        equality_check = check_3(text)
        if equality_check:
            break

    return (equality_check, letter)


def check_diag(arr: list) -> tuple:
    diag1 = [arr[0][0], arr[1][1], arr[2][2]]
    diag2 = [arr[0][2], arr[1][1], arr[2][0]]

    equality_check = False
    for row in [diag1, diag2]:
        text = ''.join(row)
        letter = text[0]
        equality_check = check_3(text)
        if equality_check:
            break

    return (equality_check, letter)


def xoreferee_checkio(game_result):
    rows = check_rows_true(game_result)
    columns = check_columns_true(game_result)
    diagonal = check_diag(game_result)

    if rows[0]:
        return rows[1]
    elif columns[0]:
        return columns[1]
    elif diagonal[0]:
        return diagonal[1]
    else:
        return "D"
