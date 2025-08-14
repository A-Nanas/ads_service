from fastapi import FastAPI
from routers import user, post
from db import models
from db.database import engine


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

@app.get("/")
def root():
    return 'OK'

models.Base.metadata.create_all(engine)