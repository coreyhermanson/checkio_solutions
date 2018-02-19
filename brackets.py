# https://py.checkio.org/mission/brackets/


def brackets_checkio(expression):
    brackets = {'{': '}', '(': ')', '[': ']', }
    chars_set = {'{', '}', '(', ')', '[', ']', }
    chars = list(filter(lambda x: x in chars_set, expression))
    stack = []

    # if no brackets, it's good
    if len(chars) == 0:
        return True

    # if number of brackets is odd, guaranteed to be bad
    elif len(chars) % 2 != 0:
        return False

    # use a stack to pop off the last opened bracket and see if it matches with the closing bracket
    else:
        for char in chars:
            if char in brackets.keys():
                stack.append(char)

            else:
                last_open_bracket = stack.pop()
                if char != brackets[last_open_bracket]:
                    return False
        return True


if __name__ == '__main__':
    assert brackets_checkio("((5+3)*2+1)") == True, "Simple"
    assert brackets_checkio("{[(3+1)+2]+}") == True, "Different types"
    assert brackets_checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert brackets_checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert brackets_checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert brackets_checkio("2+3") == True, "No brackets, no problem"
