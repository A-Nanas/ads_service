from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
from fastapi import status

from db.models import DbComment
from routers.schemas import CommentBase, UserAuth
from datetime import datetime

def create(db: Session, request: CommentBase, current_user: UserAuth):
    new_comment = DbComment(
        text = request.text,
        timestamp = datetime.now(),
        user_id = current_user.id,
        post_id = request.post_id
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(db: Session):
    return db.query(DbComment).all()

def get_comments_for_post_with_id(id: int, db: Session):
    comments = db.query(DbComment).filter(DbComment.post_id==id).all()
    return comments

def delete(id: int, db: Session, current_user): #authorise
    comment = db.query(DbComment).filter(DbComment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')
    if comment.user_id != current_user.id and not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Only comment creator can delete it')

    db.delete(comment)
    db.commit()
    return 'Ok'

def sudo_delete(id: int, db: Session): #authorise
    comment = db.query(DbComment).filter(DbComment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Post with id {id} not found')

    db.delete(comment)
    db.commit()
    return 'Ok'