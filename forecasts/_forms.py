from wtforms import Form, StringField


class ForecastSetup(Form):
    city_name = StringField(
        id="city_name",
        name="city_name",
        default=""
    )
