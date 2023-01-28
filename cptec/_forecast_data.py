import requests
import xmltodict

import msg


def get_forecast_data(city_code: int) -> dict:
    url = (
        f'http://servicos.cptec.inpe.br/XML/cidade/7dias/'
        f'{city_code}'
        f'/previsao.xml'
    )
    try:
        response = requests.get(url)
        forecast_data = xmltodict.parse(response.content)
    except requests.RequestException as err:
        msg.UNKNOWN_ERROR(err.strerror)
        raise ValueError
    if forecast_data['cidade']['nome'] == 'null':
        msg.INVALID_CITY_CODE(city_code)
        raise ValueError
    return forecast_data
