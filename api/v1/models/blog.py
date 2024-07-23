#!/usr/bin/env python3
"""The Blog Post Model."""

from sqlalchemy import (
        Column,
        Integer,
        String,
        Text,
        Numeric,
        DateTime,
        func,
        )
from datetime import datetime
from sqlalchemy import Column, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from api.v1.models.base import Base
from api.v1.models.base_model import BaseModel
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from uuid_extensions import uuid7


class Blog(BaseModel, Base):
    __tablename__ = "blogs"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid7)
    author_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )
    title = Column(String(100), nullable=False)
    content = Column(Text)
    image_url = Column(String(100), nullable=True)
    tags = Column(ARRAY(String(20)), nullable=True)
    is_deleted = Column(Boolean, default=False, nullable=False)
    excerpt = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    author = relationship("User", backref="blogs")
