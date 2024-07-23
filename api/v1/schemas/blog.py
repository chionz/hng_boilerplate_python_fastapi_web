from pydantic import BaseModel, Field
from uuid_extensions import uuid7
from uuid import UUID
import re



class BlogCreate(BaseModel):
    author_id: UUID
    title: str = Field(..., max_length=100)
    content: str
    image_url: str = None
    tags: list[str] = None
    excerpt: str = Field(None, max_length=500)