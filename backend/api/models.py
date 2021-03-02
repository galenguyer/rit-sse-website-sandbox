"""
Defines models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy_serializer import SerializerMixin

from . import db

#pylint: disable=too-few-public-methods
class Link(db.Model, SerializerMixin):
    __tablename__ = 'links'
    shortLink = Column(String(255), primary_key=True)
    longLink = Column(String(255))
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    description = Column(String(255))
    public = Column(Boolean, default=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()



"""
                          Table "public.links"
   Column    |           Type           | Collation | Nullable | Default 
-------------+--------------------------+-----------+----------+---------
 shortLink   | character varying(255)   |           | not null | 
 longLink    | character varying(255)   |           | not null | 
 createdAt   | timestamp with time zone |           |          | 
 updatedAt   | timestamp with time zone |           |          | 
 description | character varying(255)   |           |          | 
 public      | boolean                  |           | not null | false
Indexes:
    "links_pkey" PRIMARY KEY, btree ("shortLink")
"""