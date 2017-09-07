from flask import Blueprint, request, Response
from dayoff.requests import SlackCommandRequest
from dayoff.handlers import *
from datetime import datetime


blueprint = Blueprint('dayoff', __name__)

@blueprint.route('/dayoff', methods=['POST'])
def dayoff():

    validator = SlackCommandRequest(request.form)
    if not validator.validate():
        return Response(status=400)

    input = request.form['text'].strip()
    if input == 'help':
        HelpRequestHandler(request.form)
        return Response(status=202)
    if input == 'ls':
        LsRequestHandler(request.form)
        return Response(status=202)
    if _is_date(input):
        NewDayOffRequestHandler(request.form)
        return Response(status=202)

    return Response(status=400)

def _is_date(input):
    try:
        if datetime.strptime(input, '%Y-%m-%d').date():
            return True
    except ValueError:
        return False
