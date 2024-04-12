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
async def read_all_books():
    return {'data': BOOKS}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    return {'data': book}


@app.get("/books/")
async def read_category_by_query(category: str):
    books = [book for book in BOOKS if book['category'].casefold() == category.casefold()]
    return {'data': books}


@app.get("/books/{book_id}/")
async def read_book_by_query(book_id: int, category: str):
    book = next((book for book in BOOKS if book['id'] == book_id and
                 book['category'].casefold() == category.casefold()), None)

    return {'data': book}


@app.post("/books")
async def create_book(book: dict):
    BOOKS.append(book)
    return {'data': BOOKS}


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: dict):
    for i, b in enumerate(BOOKS):
        if b['id'] == book_id:
            BOOKS[i] = book
            return {'data': BOOKS}


@app.patch("/books/{book_id}")
async def update_book(book_id: int, book: dict):
    for i, b in enumerate(BOOKS):
        if b['id'] == book_id:
            BOOKS[i].update(book)
            return {'data': BOOKS}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, b in enumerate(BOOKS):
        if b['id'] == book_id:
            del BOOKS[i]
            return {'data': BOOKS}


if __name__ == "__main__":
    uvicorn.run("books:app", host="127.0.0.1", port=5000, reload=True)

# uvicorn books:app --reload
# swagger: localhost:5000/docs
