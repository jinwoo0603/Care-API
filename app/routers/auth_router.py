from fastapi import APIRouter, Depends, HTTPException, Header
from typing import Annotated

from app.models.request_model import AuthSignupReq, AuthSigninReq
from app.dependencies.db import get_db_session
from app.dependencies.cache import *
from app.services.jwt_service import JWTService
from app.services.auth_service import AuthService

router = APIRouter(prefix='/auth')

@router.post('/signup')
def post_signup(req: AuthSignupReq,
                db=Depends(get_db_session),
                jwtService: JWTService=Depends(),
                authService: AuthService=Depends(),
                cache = Depends(get_cache)):

    user = authService.signup(db, req.login_id, req.pwd, req.name)
    
    if not user:
        raise HTTPException(status_code=400, detail="ERROR")
    
    access_token = jwtService.create_token(user.model_dump())
   
    user.access_token = access_token

    redis_key = f"user:{user.id}" 
    cache.setex(redis_key, 3600, access_token)

    return user


@router.post("/signin")
def post_signin(req: AuthSigninReq, 
                db=Depends(get_db_session),
                jwtService: JWTService=Depends(),
                authService: AuthService=Depends(),
                cache=Depends(get_cache)):
    user = authService.signin(db, req.login_id, req.pwd)
    if not user:
        raise HTTPException(status_code=401, detail="로그인 실패")

    access_token = jwtService.create_token(user.model_dump())
    user.access_token = access_token

    redis_key = f"user:{user.id}" 
    cache.setex(redis_key, 3600, access_token)

    return user

@router.post('/signout')
def post_signout(Authorization: Annotated[str, Header()],
                 jwtService: JWTService = Depends(),
                 cache=Depends(get_cache)):
    token = Authorization.replace('Bearer ', '')
    userDict = jwtService.decode_token(token)

    # 토큰이 유효하지 않으면 에러 반환
    if userDict is None:
        raise HTTPException(status_code=401, detail="Invalid Token")

    nUserId = userDict.get('id', 0)

    # Redis에서 해당 유저의 토큰 삭제
    redis_key = f"user:{nUserId}"
    cache.delete(redis_key)

    return {"message": "Successfully signed out"}

# /auth/me
# {'name': 'linux'}
@router.get('/me')
def get_me(Authorization: Annotated[str, Header()],
           jwtService: JWTService = Depends(),
           cache = Depends(get_cache)):
    token = Authorization.replace('Bearer ', '')
    userDict = jwtService.decode_token(token)
    if userDict is None:
        raise HTTPException(status_code=401, detail="Invaild Token")


    nUserId = userDict.get('id', 0)
    userName = userDict.get('name', '')
    # 검증이 완료됐다.

    # Redis에 저장된 토큰이 있는지 검사해본다.
    strBlackKey = f'user:{nUserId}'
    ret = cache.get(strBlackKey)
    if ret is None:
        raise HTTPException(status_code=401, detail="unauthorized")

    # Todo

    return {'user': userDict, 'ret': ret}

@router.patch('/me')
def patch_me():
    pass