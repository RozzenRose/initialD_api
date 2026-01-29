from datetime import datetime, timedelta, timezone
import jwt
from app.config import settings
from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/token')


async def create_access_token(id: int, email: str, expires_delta: timedelta):
    payload = {'id': id,
               'email': email,
               'exp': datetime.now(timezone.utc) + expires_delta}
    payload['exp'] = int(payload['exp'].timestamp())
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)   #Создание токена


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm]) #Декодирование токена
    id: str | None = payload.get('id')
    email: str | None = payload.get('email')
    expire: int | None = payload.get('exp')

    current_time = datetime.now(timezone.utc).timestamp()

    return {'id': id,
            'email': email,
            'expire': expire > current_time}


async def create_refresh_token(email: str) -> str:
    payload = {'reg': True,
               'email': email,
               'exp': datetime.now(timezone.utc) + timedelta(weeks=1)}
    token = jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
    return token


async def verify_refresh_token(token: str) -> str | None:
    payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    if payload.get('reg'):
        return payload.get('email')
    else:
        return False

