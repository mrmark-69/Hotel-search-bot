from all_requests.universal_request import *


def get_detail(hotel_id: int) -> Dict:
    """
    Получаю информацию о конкретном отеле. Название, адрес, рейтинг, фотографии и описание фотографий.
    :param hotel_id:
    :return Dict:
    """
    method_type = 'POST',
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "propertyId": hotel_id
    }
    base = api_request(method_endswith='properties/v2/detail', method_type=method_type, payload=payload)

    try:
        rate = base['data']['propertyInfo']['summary']['overview']['propertyRating']['rating']
        add = base['data']['propertyInfo']['summary']['location']['address']['addressLine']
    except TypeError:
        rate = 'не указан'
        add = 'не указан'
    hotel_detail = dict(
        address=add,  # адрес отеля
        rating=rate,  # рейтинг отеля
        images={photo['image']['url']: photo['image']['description'] for i, photo in
                enumerate(base['data']['propertyInfo']['propertyGallery']['images']) if
                i < 10})  # фотографии и описание
    return hotel_detail
