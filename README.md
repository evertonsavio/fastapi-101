## Fastapi 101

* uvicorn books:app --reload
* swagger: localhost:5000/docs

> Curl commands
```
curl -X GET localhost:5000/books
curl -X GET localhost:5000/books/1
curl -X GET localhost:5000/books/?category=Fiction
curl -X GET localhost:5000/books/1/?category=Fiction
curl -X POST localhost:5000/books -H "Content-Type: application/json" -d '{"id": 5, "title": "The Lean Startup TYPO", "author": "Eric Ries", "category": "Non-Fiction"}'
curl -X PUT localhost:5000/books/5 -H "Content-Type: application/json" -d '{"id": 5, "title": "The Lean Startup", "author": "Eric Ries", "category": "Non-Fiction"}'
curl -X PATCH localhost:5000/books/5 -H "Content-Type: application/json" -d '{"title": "The Lean Startup"}'
curl -X DELETE localhost:5000/books/5
``` 
