from fastapi import FastAPI
from routers import user, post, comment
from auth import authentication
from db import models
from db.database import engine


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

@app.get("/")
def root():
    return 'OK'

models.Base.metadata.create_all(engine)