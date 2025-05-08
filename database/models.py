from datetime import date

from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    daily_count = Column(Integer, default=0)
    is_premium = Column(Boolean, default=False)
    session_path = Column(String(255), nullable=True)
    first_seen = Column(Date, default=date.today)
    subscription_expires = Column(Date, nullable=True)

    def __repr__(self):
        return f"<User telegram_id={self.telegram_id}>"
