from pydantic import BaseModel, EmailStr
from typing import Optional

class UserOut(BaseModel):
    _id: str
    name: str
    email: str
    password: str 
    age: int
    token: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    birthdate: str 

class GetUser(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None