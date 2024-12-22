from pydantic import BaseModel
from typing import List
from datetime import date

users = [
    {"id": 1, "Name": "John Doe", "email": "john.doe@example.com", "is_active": True},
    {"id": 2, "Name": "Caleb Stone", "email": "Caleb.stone@example.com", "is_active": True},
]
books = [
    {"id": 1, "Title": "The Rising Sun", "author": "Clement Ugwu", "is_available": True},
    {"id": 2, "Title": "Purle Hibiscus", "author": "Chimamanda Adichie", "is_available": True},
]
borrow_records = []



# Pydantic models for request validation
class BorrowRequest(BaseModel):
    user_id: int
    book_id: int

class ReturnRequest(BaseModel):
    user_id: int
    book_id: int

    
