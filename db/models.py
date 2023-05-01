from sqlalchemy import Column, Integer, String
from .database import Base


class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    url = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
