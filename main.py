from database import engine, Base, SessionLocal
import models
from models import Author, Book
from sqlalchemy.orm import joinedload
from sqlalchemy import text

# создаём таблицы
Base.metadata.create_all(bind=engine)

# создаём сессию
session = SessionLocal()

# -------- Lazy --------
print("\n--- Lazy Loading ---")

authors = session.query(Author).all()

for author in authors:
    print(author.name)
    for book in author.books:
        print("-", book.title)


# -------- Eager --------
print("\n--- Eager Loading (joinedload) ---")

authors = (
    session.query(Author)
    .options(joinedload(Author.books))
    .all()
)

for author in authors:
    print(author.name)
    for book in author.books:
        print("-", book.title)

from models import User

print("\n--- Transaction + Rollback ---")

try:
    user1 = User(username="user1", email="test@mail.com")
    user2 = User(username="user2", email="test2@mail.com")

    # ❗ намеренная ошибка (одинаковый email)
    user3 = User(username="user3", email="test@mail.com")

    session.add_all([user1, user2, user3])
    session.commit()

except Exception as e:
    print("Ошибка произошла:", e)
    session.rollback()
    print("Сделан rollback (откат)")

    users = session.query(User).all()

    print("Пользователи после rollback:")
    for user in users:
        print(user.username, user.email)

    print("Количество пользователей:", len(users))

    from repository import BookRepository

    print("\n--- Repository pattern ---")

    repo = BookRepository()

    # добавляем новую книгу автору с id=1
    new_book = repo.add_book("Детство", 1)
    print("Добавлена книга:", new_book.title)

    # получаем все книги автора с id=1
    books = repo.get_books_by_author(1)

    print("Книги автора с id=1:")
    for book in books:
        print("-", book.title)

    # удаляем добавленную книгу
    repo.delete_book(new_book.id)
    print("Книга удалена:", new_book.title)

    repo.close()
print("\n--- SQLAlchemy Core ---")

result = session.execute(text("""
SELECT authors.name, COUNT(books.id) AS book_count
FROM authors
LEFT JOIN books ON authors.id = books.author_id
GROUP BY authors.name
"""))

for row in result:
    print(row)

session.close()