from typing import Optional

from pydantic import BaseModel, Field


class Book:

    book_id: int
    title: str
    author: str
    description: str
    rating: float
    year: int

    def __init__(self, book_id: int, title: str, author: str, description: str, rating: float, year: int):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.year = year


class BookRequest(BaseModel):
    book_id: Optional[int] = Field(title='id is not required')
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    description: str = Field(None, min_length=0, max_length=1000)
    rating: float = Field(..., ge=0, le=10)
    year: int = Field(..., ge=0)

    class Config:
        schema_extra = {
            "example": {
                "title": "The Da Vinci Code",
                "author": "Dan Brown",
                "description": None,
                "rating": 4.2,
                "year": 2003
            }
        }


class PatchBookRequest(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=0, max_length=1000)
    rating: Optional[float] = Field(None, ge=0, le=10)
    year: Optional[int] = Field(None, ge=0)

