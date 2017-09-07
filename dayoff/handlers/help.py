from .t import T
from dayoff.models import AccessToken
from .slack_missive import SlackMissive


class HelpRequestHandler(T):

    def __init__(self, req):
        super().__init__(req)

    def handle(self, req):
        access_token = AccessToken.query.filter_by(team_id=req['team_id']).first()
        if not access_token:
            raise AccessTokenException(f'Access token for team_id "{team_id}" not found')

        SlackMissive(access_token, req['channel_id'], 'Need help?\n' +
                                                      '- _/dayoff YYYY-mm-dd_: take a day off at this date\n' +
                                                      '- _/dayoff ls_: list the upcoming days off of your people')
