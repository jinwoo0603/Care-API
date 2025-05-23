# parameter_models.py
from pydantic import BaseModel, Field

class AuthSigninReq(BaseModel):
    login_id: str = Field(..., min_length=3, max_length=50)
    pwd: str = Field(..., min_length=8, max_length=100)

class AuthSignupReq(BaseModel):
    login_id: str = Field(..., min_length=3, max_length=50)
    pwd: str = Field(..., min_length=8, max_length=100)
    name: str = Field(..., min_length=2, max_length=30)
    rrn: str = Field(..., min_length=8, max_length=8)
    # 추후 기타 정보 추가