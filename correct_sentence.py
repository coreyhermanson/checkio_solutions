# https://py.checkio.org/mission/correct-sentence/


def correct_sentence(text: str) -> str:
    """ returns a corrected sentence which starts with a capital letter and ends with a dot. """
    new_text = text.capitalize()

    if not new_text.endswith('.'):
        new_text += "."

    return new_text

