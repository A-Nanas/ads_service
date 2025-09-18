from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from db.database import get_db
from auth.oauth2 import get_current_user
from db import db_comment
from routers.schemas import CommentBase, CommentBase, CommentDisplay, UserAuth

router = APIRouter(
    prefix='/comment',
    tags=['comment']
)

@router.post('', response_model=CommentDisplay)
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.create(db, request, current_user)

@router.get('/all', response_model=List[CommentDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_comment.get_all(db)

@router.get('/{id}', response_model=List[CommentDisplay])
def get_comments_for_post(id: int, db: Session = Depends(get_db)):
    return db_comment.get_comments_for_post_with_id(id, db)

@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_comment.delete(id, db, current_user)