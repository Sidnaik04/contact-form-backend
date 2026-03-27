from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime, UTC

from app.db.base import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(255))
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.now(UTC))
