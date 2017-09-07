from flask import current_app, Blueprint, request, Response
from dayoff.handlers import OauthAccessRequestHandler
from dayoff.requests import OauthAccessRequest


blueprint = Blueprint('hello', __name__)

@blueprint.route('/hello', methods=['GET'])
def hello():

    validator = OauthAccessRequest(request.args)
    if not validator.validate():
        return Response(status=400)

    OauthAccessRequestHandler(request.args)

    return Response(status=202)
