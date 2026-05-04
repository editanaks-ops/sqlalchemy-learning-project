from models import Book
from database import SessionLocal


class BookRepository:

    def __init__(self):
        self.session = SessionLocal()

    def add_book(self, title, author_id):
        book = Book(title=title, author_id=author_id)
        self.session.add(book)
        self.session.commit()
        return book

    def get_books_by_author(self, author_id):
        return self.session.query(Book).filter(Book.author_id == author_id).all()

    def delete_book(self, book_id):
        book = self.session.query(Book).get(book_id)
        if book:
            self.session.delete(book)
            self.session.commit()

    def close(self):
        self.session.close()