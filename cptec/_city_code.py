import requests
import xmltodict

from . import _msg, _sanitize


def get_city_code(city_name: str) -> int:
    city_name = _sanitize.accentuated_chars(city_name)
    city_name = _sanitize.alfa_string(city_name)
    url = _get_url(city_name)
    response = requests.get(url)
    cities = xmltodict.parse(response.content)
    if cities['cidades'] is None:
        _msg.INVALID_CITY_NAME(city_name)
        raise ValueError
    for _, city in cities['cidades'].items():
        if type(city) is list:
            return city[0]['id']
        else:
            return city['id']


def _get_url(city_name: str) -> str:
    return f'http://servicos.cptec.inpe.br/XML/listaCidades?city={city_name}'
