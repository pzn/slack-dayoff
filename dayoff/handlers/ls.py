from .t import T
from dayoff.models import AccessToken
from dayoff.exceptions import AccessTokenException
from .slack_missive import SlackMissive


class LsRequestHandler(T):

    def __init__(self, req):
        super().__init__(req)

    def handle(self, req):
        from dayoff import period_service


        access_token = AccessToken.query.filter_by(team_id=req['team_id']).first()
        if not access_token:
            raise AccessTokenException(f'Access token for team_id "{team_id}" not found')

        entities = period_service.upcoming_periods(access_token.id)
        if len(entities) == 0:
            message = 'No upcoming days off!'
        else:
            message = 'Upcoming days off:\n'
            for e in entities:
                message += f'- {e.user_name} on {str(e.start.date())}\n'

        SlackMissive(access_token, req['channel_id'], message)
