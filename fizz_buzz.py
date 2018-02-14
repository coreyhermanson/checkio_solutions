# https://py.checkio.org/mission/fizz-buzz/


def fizzbuzz_checkio(number):
    if (number % 5 == 0) and (number % 3 == 0):
        return "Fizz Buzz"

    elif number % 5 == 0:
        return "Buzz"

    elif number % 3 == 0:
        return "Fizz"

    else:
        return str(number)
