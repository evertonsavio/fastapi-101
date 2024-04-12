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

# uvicorn books:app --reload
# swagger: localhost:8000/docs
