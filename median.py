from statistics import median


def easy_way(data):
    return median(data)


def median_checkio(data):
    sorted_list = sorted(data)
    mid = len(data) // 2

    if len(data) % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]
