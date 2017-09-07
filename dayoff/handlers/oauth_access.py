from flask import current_app
from dayoff import db
from dayoff.models import AccessToken
from .t import T
from dayoff.exceptions import OauthAccessException
import requests


class OauthAccessRequestHandler(T):

    def __init__(self, req):
        self.client_id = current_app.config.get('SLACK_APP_CLIENT_ID')
        self.secret = current_app.config.get('SLACK_APP_CLIENT_SECRET')
        self.oauth_access_url = current_app.config.get('SLACK_OAUTH_ACCESS_URL')
        super().__init__(req)

    def handle(self, req):

        r = requests.get(url=self.oauth_access_url,
                         params=self._build_query_params(req))

        if r.status_code != 200:
            raise OauthAccessException('Could not get OAuth access', r.content)

        json = r.json()
        if json['ok'] == False:
            raise OauthAccessException('Could not get OAuth access', r.content)

        authorization_details = {
            'access_token': json['access_token'],
            'scope': json['scope'],
            'team_name': json['team_name'],
            'team_id': json['team_id']}
        self._save_team(authorization_details)

    def _build_query_params(self, req):
        return {'client_id': self.client_id,
                'client_secret': self.secret,
                'code': req['code']}

    def _save_team(self, authorization_details):
        access_token = AccessToken()
        access_token.access_token = authorization_details['access_token']
        access_token.scope = authorization_details['scope']
        access_token.team_name = authorization_details['team_name']
        access_token.team_id = authorization_details['team_id']
        db.session.add(access_token)
        db.session.commit()
