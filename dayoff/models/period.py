from .base import Base
from sqlalchemy import UniqueConstraint
from dayoff import db


class Period(Base):

    user_id = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    start = db.Column(db.DateTime(), nullable=False)
    reason = db.Column(db.String(255), nullable=True)
    access_token_id = db.Column(db.Integer(), db.ForeignKey("access_token.id"))
    __table_args__ = (
        UniqueConstraint('user_id', 'start', name='_user_id_start_uq'),
        )
