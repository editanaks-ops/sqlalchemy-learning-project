from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")

class User(Base):
        __tablename__ = "users"

        id = Column(Integer, primary_key=True)
        username = Column(String, nullable=False)
        email = Column(String, unique=True, nullable=False)

        from sqlalchemy import DateTime
        from datetime import datetime

        class Order(Base):
            __tablename__ = "orders"

            id = Column(Integer, primary_key=True)
            product_name = Column(String, nullable=False)
            quantity = Column(Integer, nullable=False)
            price = Column(Float)