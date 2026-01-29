from app.database.engine import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    rus = Column(String)
    eng = Column(String)

    user_words = relationship(
        "UserWords",
        back_populates="word",
        cascade="all, delete-orphan"
    )