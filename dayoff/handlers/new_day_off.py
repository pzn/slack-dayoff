from .t import T
from dayoff.models import AccessToken
from dayoff.exceptions import AccessTokenException
from .slack_missive import SlackMissive
from datetime import datetime


class NewDayOffRequestHandler(T):

    def __init__(self, req):
        super().__init__(req)

    def handle(self, req):
        from dayoff import period_service


        access_token = AccessToken.query.filter_by(team_id=req['team_id']).first()
        if not access_token:
            raise AccessTokenException(f'Access token for team_id "{team_id}" not found')

        date = self._to_date(req['text'].strip())
        if date <= datetime.now().date():
            SlackMissive(access_token, req['channel_id'], 'Do you really want a day off in the past Dr. Emmett Brown?')
            return

        try:
            period_service.add_period(user_id=req['user_id'],
                                      user_name=req['user_name'],
                                      start=date,
                                      team_id=req['team_id'])
        except Exception as e:
            SlackMissive(access_token, req['channel_id'], f'Error while adding your day off @{req["user_name"]}. Are you already off on this day?')
            return

        SlackMissive(access_token, req['channel_id'], f'@{req["user_name"]} just took a day off on {date}')

    def _to_date(self, input):
        return datetime.strptime(input, '%Y-%m-%d').date()
