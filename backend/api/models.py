"""
Defines models
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

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

class Quote(db.Model, SerializerMixin):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    body = Column(String)
    description = Column(String)
    approved = Column(Boolean, default=False)
    tags = relationship('Tag')

    @classmethod
    def get_all(cls):
        return cls.query.all()

class Tag(db.Model, SerializerMixin):
    __tablename__ = 'quotes_tags'
    tagName = Column(String(255), primary_key=True)
    quoteId = Column(ForeignKey('quotes.id'), primary_key=True)
