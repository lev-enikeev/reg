# python -m uvicorn main:app --reload
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import db

origins = [
    "http://localhost",
    "http://localhost:5500",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Auth(BaseModel):
    email: str
    password: str


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.post('/register')
def register(auth: Auth):
    if auth.email in db.get_all_users():
        return {'erorr': 'user exists'}
    db.insert_new_user(auth.email, auth.password)
    return {'msg': 'success'}


@app.post("/login")
def post(auth: Auth):
    pass
