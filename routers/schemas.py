from pydantic import BaseModel
from datetime import datetime


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
    creator_id: int

    def __str__(self):
        return f"{self.title}, {self.text}, {self.creator_id}"

#for Post Display:

class User(BaseModel):
    username: str
    class Config():
        from_attributes = True


class PostDisplay(BaseModel):
    title: str
    text: str
    timestamp: datetime
    user: User
    class Config():
        from_attributes = True