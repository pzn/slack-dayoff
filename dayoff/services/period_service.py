from dayoff.models import AccessToken, Period
from dayoff.exceptions import AccessTokenException
from sqlalchemy import func
from datetime import datetime


class PeriodService:

    def __init__(self, db):
        self.db = db

    def add_period(self, user_id, user_name, start, team_id):
        access_token = AccessToken.query.filter_by(team_id=team_id).first()
        if not access_token:
            raise AccessTokenException(f'Access token for team_id "{team_id}" not found')
        period = Period()
        period.user_id = user_id
        period.user_name = user_name
        period.start = start
        period.access_token_id = access_token.id
        try:
            self.db.session.add(period)
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e

    def upcoming_periods(self, access_token_id, limit=3):
        now = '{0:%Y-%m-%d}'.format(datetime.utcnow())
        periods = Period.query.\
                  filter_by(access_token_id=access_token_id).\
                  filter(Period.start >= now).\
                  order_by(Period.start).\
                  limit(limit).all()
        return periods
