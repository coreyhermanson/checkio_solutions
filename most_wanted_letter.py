from collections import Counter


def most_wanted_letter_checkio(text):
    letters = [letter for letter in text.lower() if letter.isalpha()]
    letter_counter = Counter(letters)
    most_common = letter_counter.most_common()

    maximum = most_common[0][1]
    letter_list = list(most_common[0][0])

    for i in most_common[1:]:
        if i[1] == maximum:
            letter_list.extend(i[0])
        else:
            break

    sorted_letter_list = sorted(letter_list)
    most_common_letter = sorted_letter_list[0]

    return most_common_letter
