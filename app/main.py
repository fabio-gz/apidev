from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)



app = FastAPI()



class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_post = []

@app.get("/")
def root():
    return {'message': 'hello world'}

@app.get('/sqlalchemy')
def test_post(db: Session = Depends(get_db)):

    post = db.query(models.Post).all()
    return {'data': post}

@app.get('/posts')
def get_posts():
    return {'data': 'this is your post'}


@app.post('/posts')
def create_posts(post: Post):
    print(post.published)
    return{"data": "post"}