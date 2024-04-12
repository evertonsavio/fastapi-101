import uvicorn
from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'id': 1, 'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'category': 'Fiction'},
    {'id': 2, 'title': 'The Alchemist', 'author': 'Paulo Coelho', 'category': 'Fiction'},
    {'id': 3, 'title': 'The Godfather', 'author': 'Mario Puzo', 'category': 'Fiction'},
    {'id': 4, 'title': 'The Lean Startup', 'author': 'Eric Ries', 'category': 'Non-Fiction'},
]


@app.get("/books")
def read_all_books():
    return {'data': BOOKS}


@app.get("/books/{book_id}")
def read_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    return {'data': book}


@app.get("/books/")
def read_category_by_query(category: str):
    books = [book for book in BOOKS if book['category'].casefold() == category.casefold()]
    return {'data': books}


@app.get("/books/{book_id}/")
def read_book_by_query(book_id: int, category: str):
    book = next((book for book in BOOKS if book['id'] == book_id and
                 book['category'].casefold() == category.casefold()), None)

    return {'data': book}


@app.post("/books")
def create_book(book: dict):
    BOOKS.append(book)
    return {'data': BOOKS}


if __name__ == "__main__":
    uvicorn.run("books:app", host="127.0.0.1", port=5000, reload=True)

# uvicorn books:app --reload
# swagger: localhost:5000/docs

# curl -X GET localhost:5000/books
# curl -X GET localhost:5000/books/1
# curl -X GET localhost:5000/books/?category=Fiction
# curl -X GET localhost:5000/books/1/?category=Fiction
# curl -X POST localhost:5000/books -H "Content-Type: application/json" -d '{"id": 5, "title": "The Lean Startup", "author": "Eric Ries", "category": "Non-Fiction"}'
