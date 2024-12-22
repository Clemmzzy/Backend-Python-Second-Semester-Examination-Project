from fastapi import APIRouter, HTTPException
from typing import List
from schemas.Book import Book, Books

Book_router = APIRouter()

# Get all Books
@Book_router.get("/", response_model=List[Book], status_code=200)
def get_all_Books():
    return Books

# Create a Book
@Book_router.post("/", status_code=201)
def create_Book(Book: Book):
    if any(u["id"] == Book.id for u in Books):
        raise HTTPException(status_code=400, detail="Book ID already exists.")
    Books.append(Book.model_dump())
    return Book


# Get a specific Book
@Book_router.get("/{Book_id}", response_model=Book, status_code=200)
def get_Book(Book_id: int):
    Book = next((u for u in Books if u["id"] == Book_id), None)
    if not Book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return Book

# Update a Book
@Book_router.put("/{Book_id}", response_model=Book, status_code=200)
def update_Book(Book_id: int, updated_Book: Book):
    for i, Book in enumerate(Books):
        if Book["id"] == Book_id:
            Books[i] = updated_Book.model_dump()
            return updated_Book
    raise HTTPException(status_code=404, detail="Book not found.")

# Delete a Book
@Book_router.delete("/{Book_id}", status_code=204)
def delete_Book(Book_id: int):
    global Books
    Books = [u for u in Books if u["id"] != Book_id]
    return {"message": "Book deleted successfully."}

# Book Availability
@Book_router.patch("/{Book_id}/Availability", status_code=200)
def Availability(Book_id: int):
    Book = next((u for u in Books if u["id"] == Book_id), None)
    if Book:
        raise HTTPException(status_code=200, detail="Book is Available")
    if not Book:
        raise HTTPException(status_code=404, detail="Book Is not Available.")
    Book["is_active"] = False
    return {"message": "Book is unavailable."}