from app.database.engine import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)

    user_words = relationship(
        "UserWords",
        back_populates="user",
        cascade="all, delete-orphan"
    )