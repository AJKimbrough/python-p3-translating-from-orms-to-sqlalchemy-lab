#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, Index)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    Index('index_name', 'name')

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
