import flask


def INVALID_CITY_CODE(city_code: int):
    flask.flash(
        f'O código da cidade "{city_code}" é inválido para obter as previsões',
        'warning'
    )

def INVALID_CITY_NAME(city_name: str):
    flask.flash(
        f'Não foi encontrado nenhum código de cidade válido para "{city_name}"',
        'warning'
    )

def UNKNOWN_ERROR(error: str):
    flask.flash(error, 'danger')
