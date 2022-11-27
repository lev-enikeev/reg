# python -m uvicorn main:app --reload
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from helpers import encode_email, decode_email
from mail import send_email
import db

origins = [
    "*"
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
    url = encode_email(auth.email)
    send_email(url, auth.email)
    return {'msg': 'success'}


@app.get('/confirm/')
def confirm(email: str):
    email = decode_email(email)
    db.update_email(email)
    return {'msg': 'success'}


@app.post("/login")
def post(auth: Auth):
    pass
