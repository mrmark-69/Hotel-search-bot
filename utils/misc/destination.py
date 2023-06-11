from typing import List


def destination(hotels: List) -> List:
    sorted_list = list()
    for hotel in sorted(hotels, key=lambda x: x['distance_from']):
        sorted_list.append(hotel)
    return sorted_list
