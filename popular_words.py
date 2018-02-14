# https://py.checkio.org/mission/popular-words/

from collections import Counter
import re


def popular_words(text, words):
    text_lower = text.lower()
    regex = r'[\w\']+|[.,!?;]'
    word_list = re.findall(regex, text_lower)
    counted = Counter(word_list)
    new_dict = {}

    for i in words:
        new_dict[i] = counted[i]

    print(new_dict)

    return new_dict
