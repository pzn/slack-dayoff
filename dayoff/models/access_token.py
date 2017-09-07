from .base import Base
from dayoff import db


class AccessToken(Base):

    access_token = db.Column(db.String(255),nullable=False,
                             unique=True)
    scope = db.Column(db.String(255), nullable=False)
    team_name = db.Column(db.String(255), nullable=False)
    team_id = db.Column(db.String(255), nullable=False)
