from datetime import datetime

import pandas as pd

import cptec
from . import _format, _config


class Weatherman:
    def __init__(self, city_name: str):
        city_code = cptec.get_city_code(city_name)
        forecast_data = cptec.get_forecast_data(city_code)
        print(forecast_data)
        self._forecast_data = forecast_data


    @property
    def forecasts(self) -> dict:
        out = []
        city_name = self._forecast_data['cidade']['nome']
        district_name = self._forecast_data['cidade']['uf']
        for fc in self._forecast_data['cidade']['previsao']:
            fc['dia'] = datetime.strptime(fc['dia'], '%Y-%m-%d')
            fc['maxima'] = f"{fc['maxima']}°C"
            fc['minima'] = f"{fc['minima']}°C"
            out.append(fc)
        df = pd.DataFrame(out)
        df['dia'] = df['dia'].apply(func=_format.weather_day)
        df['tempo'] = df['tempo'].apply(func=_format.weather_emoji)
        df.drop(columns=['iuv'], inplace=True)
        df.rename(columns=_config.table_headers, inplace=True)
        return {
            'city_name': city_name,
            'district_name': district_name,
            'forecasts': _format.weather_html(df)
        }
