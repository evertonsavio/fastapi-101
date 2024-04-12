from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {'id': 1, 'title': 'The Da Vinci Code', 'author': 'Dan Brown'},
    {'id': 2, 'title': 'The Alchemist', 'author': 'Paulo Coelho'},
    {'id': 3, 'title': 'The Godfather', 'author': 'Mario Puzo'}
]


@app.get("/books")
async def read_all_books():
    return {'data': BOOKS}


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = next((book for book in BOOKS if book['id'] == book_id), None)
    return {'data': book}


# uvicorn books:app --reload
# swagger: localhost:8000/docs
