from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies.db import create_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

origins = [
    "http://localhost:3000", # 나중에 https 구현하면 지울것
    "https://localhost:3000",
    # 배포시 URL 추가
]

app = FastAPI(lifespan=lifespan)

# 추후 라우터 추가

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
