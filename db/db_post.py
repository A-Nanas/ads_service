from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from db.models import DbPost, DbComment
from db.db_comment import sudo_delete
from routers.schemas import PostBase
from datetime import datetime


def create(db: Session, request: PostBase, current_user):
    new_post = DbPost(
        title = request.title,
        text = request.text,
        timestamp = datetime.now(),
        user_id = current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DbPost).all()

def delete(id: int, db: Session, current_user): #authorise
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    if post.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only post creator can delete it')
    print(post.user_id, current_user.id, current_user.is_admin)
    comments = db.query(DbComment).filter(DbComment.post_id == post.id).all()
    for comment in comments:
        sudo_delete(comment.id, db)
    db.delete(post)
    db.commit()
    return 'Ok'