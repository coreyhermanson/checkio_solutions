def house_password_checkio(data: str) -> bool:
    # 'all' returns True is all values in iterator are True
    check = all([
        # check is alphanumeric
        data.isalnum(),
        #  check length => 10
        len(data) >= 10,
        # at least 1 digit
        any(char.isdigit() for char in data),
        # at least 1 uppercase letter
        any(char.isupper() for char in data),
        # at least 1 lowercase letter
        any(char.islower() for char in data)
    ])

    return check
