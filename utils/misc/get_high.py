from typing import List


def high_price(number_of_hotels: int, hotels: List) -> List:
    reversed_list = list()
    count = 0
    for hotel in sorted(hotels, key=lambda x: int(x['rounded_price']),
                        reverse=True):  # Лямбда функция сортирует отели по цене, от высокой к низкой.
        if count < number_of_hotels:
            reversed_list.append(hotel)
            count += 1
    return reversed_list
