# https://py.checkio.org/mission/three-words/
import re


def three_words_checkio(words: str) -> bool:
    regex = r'([A-Za-z]+ ){2}[A-Za-z]+'
    match = re.search(regex, words)
    return bool(match)
