from wtforms import Form, StringField, validators


# curl localhost:5000/hello?code=my_code&state=my_state

class OauthAccessRequest(Form):
    code = StringField('code', [validators.DataRequired()])
    state = StringField('state', [validators.Optional()])
