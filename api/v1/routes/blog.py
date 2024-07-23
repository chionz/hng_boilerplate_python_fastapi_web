from fastapi import APIRouter, Depends, Security, HTTPException, Query
from sqlalchemy.orm import Session
from api.db.database import get_db
from api.v1.schemas.blog import BlogCreate
from api.v1.models.blog import Blog

blog = APIRouter()




@blog.post("/api/v1/blog")
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = Blog(
        author_id=blog.author_id,
        title=blog.title,
        content=blog.content,
        image_url=blog.image_url,
        tags=blog.tags,
        excerpt=blog.excerpt
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
