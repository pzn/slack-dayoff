from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

from .controllers import HelloBlueprint, DayOffBlueprint
app.register_blueprint(HelloBlueprint)
app.register_blueprint(DayOffBlueprint)

from .services import PeriodService
period_service = PeriodService(db)

@app.after_request
def after_request(response):
    response.headers['Content-Type']='application/json'
    return response
