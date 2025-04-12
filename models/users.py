from sqlalchemy import Boolean, Column, Integer, String
from Training.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,unique=True, index=True)
