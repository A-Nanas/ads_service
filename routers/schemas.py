from pydantic import BaseModel
from datetime import datetime
from typing import List


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config():
        from_attributes = True


class PostBase(BaseModel):
    title: str
    text: str

#for Post Display:

class User(BaseModel):
    username: str
    class Config():
        from_attributes = True

class Comment(BaseModel):
    text: str
    user: User
    class Config():
        from_attributes = True


class PostDisplay(BaseModel):
    title: str
    text: str
    timestamp: datetime
    id: int
    user: User
    comments: List[Comment]
    class Config():
        from_attributes = True


class CommentBase(BaseModel):
    text: str
    username: str
    post_id: int
    class Config():
        from_attributes = True


class CommentDisplay(BaseModel):
    text: str
    timestamp: datetime
    user: User
    class Config():
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str