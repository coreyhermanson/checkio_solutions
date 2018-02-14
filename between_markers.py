# https://py.checkio.org/mission/between-markers/


def between_markers(text: str, begin: str, end: str) -> str:
    """ returns substring between two given markers"""

    try:
        start = text.index(begin) + len(begin)

    except ValueError:
        start = 0

    try:
        finish = text.index(end)

    except ValueError:
        finish = len(text)

    return text[start:finish]
