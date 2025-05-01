from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from app.dependencies.db import create_db
from app.routers import auth_router
from app.routers import data_router

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

app.include_router(auth_router.router)
app.include_router(data_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
