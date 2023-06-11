from typing import Any, Dict
import all_requests
from config_data.config import RAPID_API_KEY


def api_request(method_endswith,  # Меняется в зависимости от запроса. locations/v3/search либо properties/v2/list
                method_type,  # Метод\тип запроса GET\POST
                payload: Dict,  # Словарь с параметрами запроса.
                ) -> Any:
    url = f"https://hotels4.p.rapidapi.com/{method_endswith}"

    # В зависимости от типа запроса вызываем соответствующую функцию
    if method_type == 'GET':
        return get_request(
            url=url,
            payload=payload
        )
    else:
        return post_request(
            url=url,
            payload=payload
        )


def get_request(url, payload) -> str:
    try:
        response = all_requests.get(
            url=url,
            headers={
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
            },
            params=payload,
            timeout=15
        )
        if response.status_code == all_requests.codes.ok:
            return response.json()
        else:
            return f'Ошибка. Статус код: {response.status_code} {response.json()}'
    except Exception as exc:
        print(f'ErrorGET {exc}')


def post_request(url, payload):
    try:
        response = all_requests.post(
            url=url,
            json=payload,
            headers={
                "content-type": "application/json",
                "X-RapidAPI-Key": RAPID_API_KEY,
                "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
            },
            timeout=15)

        if response.status_code == all_requests.codes.ok:
            return response.json()
        else:
            return f'Ошибка. Статус код: {response.status_code} {response.json()}'
    except Exception as exc:
        print(f'ErrorPOST {exc}')
