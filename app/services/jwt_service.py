import time
import os
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('JWT_KEY')
ALG = "HS256"

class JWTService:    
    # 1. JWT Token 생성 함수
    # Payload={
    #   "id": 1,
    #   "login_id": "loiss",
    #   "name": "aaaaa",
    #   "exp":fsdfsfsdf
    # }, 유효기간
    # -> Jwt token
    def create_token(self, payload: dict,
                    expires_delta: timedelta | None = timedelta(minutes=30)):
        payload_to_encode = payload.copy()
        expire = datetime.now(timezone.utc) + expires_delta
        payload_to_encode.update({
            'exp': expire
        })
        return jwt.encode(payload_to_encode, SECRET_KEY, algorithm=ALG)

    # 2. token 문자열로 payload 만드는 함수
    def decode_token(self, token: str) -> dict | None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALG])
            return payload
        except ExpiredSignatureError:
            # 토큰이 만료됨
            return None
        except JWTError:
            # 기타 JWT 에러 (invalid signature 등)
            return None
    # 추후 refresh token 추가할것
