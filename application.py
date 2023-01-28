import flask

import forecasts


application = flask.Flask(__name__)
application.register_blueprint(forecasts.forecasts_blueprint)
application.secret_key = "algumacoisaqueprecisaserrealmentealeatoriaesegura"

@application.route("/", methods=["GET", "POST"])
def home():
    return flask.redirect(
        flask.url_for('forecasts.weather_forecast')
    )

if __name__ == '__main__':
    application.debug = True
    application.run()
