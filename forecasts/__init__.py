import flask

from . import _format, _forms
from ._weatherman import Weatherman


forecasts_blueprint = flask.Blueprint(
    'forecasts', __name__, template_folder='./html'
)

@forecasts_blueprint.route("/previsao", methods=["GET", "POST"])
def weather_forecast() -> str:
    if flask.request.method == 'GET':
        return _render_page()
    if flask.request.method == 'POST':
        data = flask.request.form
        form = _forms.ForecastSetup(data=data)
        city_name = form.city_name.data
        try:
            results = Weatherman(city_name).forecasts
        except ValueError:
            results = None
        return _render_page(form=form, results=results)


def _render_page(form=_forms.ForecastSetup(), results=None) -> str:
    return flask.render_template(
        'weather-forecast.html',
        form=form,
        results=results
    )
