import uvicorn
from fastapi import FastAPI, Path, Query, HTTPException
from starlette import status

from books.models.Book import Book, BookRequest, PatchBookRequest

app = FastAPI()

BOOKS = [
    Book(1, "The Da Vinci Code", "Dan Brown", "", 4.5, 2003),
    Book(2, "The Alchemist", "Paulo Coelho", "", 4.5, 1988),
    Book(3, "The Little Prince", "Antoine de Saint-Exupéry", "", 4.5, 1943),
    Book(4, "The Hobbit", "J.R.R. Tolkien", "", 4.5, 1937),
    Book(5, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "", 4.5, 1997),
    Book(6, "And Then There Were None", "Agatha Christie", "", 4.5, 1939),
    Book(7, "Dream of the Red Chamber", "Cao Xueqin", "", 4.5, 1791)
]


@app.get("/books", status_code=status.HTTP_200_OK)
async def read_all_books():
    return {'data': BOOKS}


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    book = next((book for book in BOOKS if book.book_id == book_id), None)
    if book:
        return {'data': book}
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_category_by_query(author: str = Query(gt=0, lt=100)):
    books = [book for book in BOOKS if book.author.casefold() == author.casefold()]
    return {'data': books}


@app.get("/books/", status_code=status.HTTP_200_OK)
async def read_rating_by_query(rating: float = Query(gt=0, lt=10)):
    books = [book for book in BOOKS if book.rating >= rating]
    return {'data': books}


@app.get("/books/{book_id}/", status_code=status.HTTP_200_OK)
async def read_book_by_query(book_id: int, author: str):
    book = next((book for book in BOOKS if book.book_id == book_id), None)
    if book:
        if book.author.casefold() == author.casefold():
            return {'data': book}
    return {'data': None}


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_book(new_book: BookRequest):
    BOOKS.append(Book(**new_book.dict()))
    return {'data': BOOKS}


@app.put("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_id: int, book: BookRequest):
    for i, b in enumerate(BOOKS):
        if b.book_id == book_id:
            BOOKS[i] = Book(**book.dict())


@app.patch("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book_id: int, book: PatchBookRequest):
    for i, b in enumerate(BOOKS):
        if b.book_id == book_id:
            for field, value in book.dict().items():
                if value is not None:
                    setattr(BOOKS[i], field, value)


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    for i, b in enumerate(BOOKS):
        if b.book_id == book_id:
            del BOOKS[i]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)

"""
curl -X 'GET' localhost:5000/books
curl -X 'GET' localhost:5000/books/1
curl -X 'GET' localhost:5000/books/?author=Dan%20Brown
curl -X 'GET' localhost:5000/books/1/?author=Dan%20Brown
curl -X 'POST' localhost:5000/books -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'PUT' localhost:5000/books/8 -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'PATCH' localhost:5000/books/8 -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'DELETE' localhost:5000/books/8
"""
