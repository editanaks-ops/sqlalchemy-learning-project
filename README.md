#  SQLAlchemy Learning Project

Backend-проект, демонстрирующий работу с:

- SQLAlchemy ORM
- Транзакциями и rollback
- Alembic миграциями
- Repository Pattern
- SQLAlchemy Core



##  Основные возможности

✔ Связи между таблицами (One-to-Many)  

✔ Управление транзакциями  

✔ Миграции базы данных  

✔ Оптимизация загрузки данных  

✔ Агрегирующие SQL-запросы  


Проект выполнен как практическая работа и отражает навыки backend-разработки.
##  Задача 1: Модели и связи

Реализованы модели:

####  Author
- `id` — первичный ключ  
- `name` — имя автора  

####  Book
- `id` — первичный ключ  
- `title` — название книги  
- `author_id` — внешний ключ  

####  Связь:
- Один автор → много книг (One-to-Many)


books = relationship("Book", back_populates="author")

 ### Результат:
Реализована двусторонняя связь
Данные успешно извлекаются через ORM
Поддерживаются:
Lazy Loading
Eager Loading (joinedload)

## Задача 2: Транзакции и откат

Реализована транзакция с контролем ошибок:

try:
    session.add_all([user1, user2, user3])
    session.commit()
except Exception:
    session.rollback()

### Сценарий:
Добавляются 2 пользователя
3-й пользователь вызывает ошибку (дубликат email)

### Результат:
Возникает IntegrityError
Выполняется rollback
В базе не сохраняется ни одной записи

✔ Гарантирована целостность данных

## Задача 3: Alembic (миграции)

 Инициализация:
alembic init alembic

 Создание таблицы Order:

Поля:

id
product_name
quantity
created_at
alembic revision --autogenerate -m "create orders table."
alembic upgrade head

### Изменение структуры:
Добавлено поле price
Удалено поле created_at
alembic revision --autogenerate -m "update orders table."
alembic upgrade head

### Откат миграции:
alembic downgrade -1

### Результат:
Миграции применяются корректно
Откат возвращает предыдущую структуру


## Задача 4: Repository Pattern

Реализован класс BookRepository.

### Методы:

add_book(title, author_id)
get_books_by_author(author_id)
delete_book(book_id)

### Особенности:
Инкапсуляция логики работы с БД
Упрощение тестирования
Чистая архитектура

### Результат:
Добавление книги
Получение книг автора
Удаление книги

## Дополнительное задание

 Логирование SQL
engine = create_engine("sqlite:///homework.db", echo=True)

Позволяет видеть реальные SQL-запросы.

 Оптимизация загрузки

Использованы стратегии:

Lazy Loading

Eager Loading (joinedload)

SQLAlchemy Core (агрегирующий запрос)

SELECT authors.name, COUNT(books.id) AS book_count

FROM authors

LEFT JOIN books ON authors.id = books.author_id

GROUP BY authors.name

### Результат:
('Лев Толстой', 2)
('Фёдор Достоевский', 2)

## Архитектура проекта
```text
sqlalchemy_homework/
│
├── database.py        # подключение к БД
├── models.py          # модели ORM
├── repository.py      # Repository pattern
├── main.py            # точка входа
│
├── alembic/           # миграции
│   ├── versions/
│   └── env.py
│
├── alembic.ini
└── homework.db
```

### Запуск проекта
```bash
python main.py
```
## Выводы

В рамках проекта:

Освоена работа с ORM и связями
Реализованы транзакции и откаты
Настроен Alembic для миграций
Применён паттерн Repository
Выполнена оптимизация запросов
Использован SQLAlchemy Core

## Итог

Проект демонстрирует:

✔ Глубокое понимание SQLAlchemy

✔ Работа с транзакциями

✔ Управление миграциями

✔ Чистую архитектуру

✔ Готовность к backend-разработке
