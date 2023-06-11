from all_requests.universal_request import *
from typing import List


def get_hotels(region, date_in, date_out, min_price, max_price) -> List or None:
    """
    С этой функцией получаю список отелей с id отеля, названием, ценой и расстоянием до центра.

    :param region:
    :param date_in:
    :param date_out:
    :param min_price:
    :param max_price:
    :return List:
    """
    method_endswith = "properties/v2/list"
    method_type = 'POST'
    day_in, month_in, year_in = date_in.day, date_in.month, date_in.year
    day_out, month_out, year_out = date_out.day, date_out.month, date_out.year
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_EU",
        "siteId": 300000001,
        "destination": {"regionId": region},
        "checkInDate": {
            "day": day_in,
            "month": month_in,
            "year": year_in
        },
        "checkOutDate": {
            "day": day_out,
            "month": month_out,
            "year": year_out
        },
        "rooms": [
            {
                "adults": 2,
                "children": [{"age": 5}, {"age": 7}]
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": 200,
        "sort": 'PRICE_LOW_TO_HIGH',
        "filters": {"price": {
            "max": max_price,
            "min": min_price
        }}
    }
    base = api_request(method_endswith=method_endswith, method_type=method_type, payload=payload)

    if base['data'] is None:
        return None
    else:
        hotel_list = []
        hotels = base['data']['propertySearch']['properties']
        for hotel in hotels:
            hotel_list.append(dict(
                id=hotel['id'],  # id отеля.
                name=hotel['name'],  # Название отеля.
                price=hotel['price']['options'][0]['formattedDisplayPrice'],  # цена за ночь.
                total_price=hotel['price']['displayMessages'][1]['lineItems'][0]['value'][:-6],
                # Цена за все время пребывания.
                distance_from=hotel['destinationInfo']['distanceFromDestination']['value'],  # Расстояние от центра.
                rounded_price=hotel['price']['lead']['amount']
            ))
        return hotel_list
