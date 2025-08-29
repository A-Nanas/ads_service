from sqlalchemy.orm import relationship

from db.database import Base

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    posts = relationship('DbPost', back_populates='user')
    comments = relationship('DbComment', back_populates='user')


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('DbUser', back_populates='posts')
    comments = relationship('DbComment', back_populates='post')


class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    post = relationship('DbPost', back_populates='comments')
    user = relationship('DbUser', back_populates='comments')
    post_id = Column(Integer, ForeignKey('post.id'))