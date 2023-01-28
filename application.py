import flask

import forecasts

application = flask.Flask(__name__)
application.register_blueprint(forecasts.forecasts_blueprint)
application.secret_key = "somethingthatneedstobereallyrandomandsecure"

if __name__ == '__main__':
    application.debug = True
    application.run()
