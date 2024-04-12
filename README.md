## Fastapi 101

* uvicorn books:app --reload
* swagger: localhost:5000/docs

> Curl commands
```
curl -X 'GET' localhost:5000/books
curl -X 'GET' localhost:5000/books/1
curl -X 'GET' localhost:5000/books/?author=Dan%20Brown
curl -X 'GET' localhost:5000/books/1/?author=Dan%20Brown
curl -X 'POST' localhost:5000/books -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'PUT' localhost:5000/books/8 -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'PATCH' localhost:5000/books/8 -H 'Content-Type: application/json' -d '{"book_id": 8, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "", "rating": 4.5, "year": 1925}'
curl -X 'DELETE' localhost:5000/books/8
``` 
