from app.database.engine import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class UserWords(Base):
    __tablename__ = "user_words"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    word_id = Column(Integer, ForeignKey("words.id"), primary_key=True)
    status = Column(String)

    user = relationship("User", back_populates="user_words")
    word = relationship("Word", back_populates="user_words")