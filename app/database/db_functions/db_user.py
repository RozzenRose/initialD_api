import json

from app.database.models import User
from app.schemas import CreateUser
from sqlalchemy import insert, select


async def create_user_in_db(db, user_data: CreateUser, hashed_password: str) -> None:
    data = insert(User).values(
        email=user_data.email,
        hashed_password=hashed_password)
    await db.execute(data)
    await db.commit()


async def get_user_from_db(db, email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalars().first()
    return user
