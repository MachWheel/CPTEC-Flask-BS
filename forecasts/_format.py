from datetime import datetime

import pandas as pd

import config.table


def weather_html(df: pd.DataFrame) -> str:
    return df.to_html(
        index=False,  # Ocultar contador de linha
        border=0,  # Atributo border (css)
        decimal=",",  # Separador de decimais para floats
        justify="left",  # Justificação dos cabeçalhos
        table_id="weather-results",  # Atributo id da tabela (css)
        classes="table table-striped text-center",  # Atributo classes da tabela (css)
    ).replace('<th>', '<th class="text-center">')

def weather_emoji(weather_code: str) -> str:
    return config.table.weather_emojis[weather_code]

def weather_day(weather_date: datetime) -> str:
    return weather_date.strftime('%d/%m')
