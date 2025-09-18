from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from auth.oauth2 import get_current_user
from db.database import get_db
from db import db_post
from routers.schemas import PostDisplay, PostBase, UserAuth

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('', response_model=PostDisplay)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.create(db, request, current_user)

@router.get('/all', response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_post.delete(id, db, current_user)