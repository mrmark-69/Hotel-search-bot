from all_requests.universal_request import *


def get_region_id(city: str) -> Dict or False:
    """
     С помощью это функции получаю словарь с regionId и названием региона,
    который использую для запроса в https://hotels4.p.rapidapi.com/properties/v2/list

    :param city:
    :return Dict:
    """
    method_endswith = "locations/v3/search"

    method_type = 'GET'
    querystring = {
        "q": city,
        "locale": "en_EU",
        "langid": "1033",
        "siteid": "300000001"}

    base = api_request(method_endswith=method_endswith, method_type=method_type, payload=querystring)

    if base is None:
        return False
    else:
        regions = base['sr']
        regions_dict = dict()
        for region in regions:
            if 'gaiaId' in region:
                regions_dict[region['gaiaId']] = region['regionNames']['displayName']
        return regions_dict
