from fastapi import APIRouter, HTTPException
from datetime import datetime
from schemas.BorrowRecord import users, books, borrow_records, BorrowRequest, ReturnRequest


Borrow_router = APIRouter()


def find_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)

def find_book_by_id(book_id):
    return next((book for book in books if book["id"] == book_id), None)

def find_active_borrow_record(user_id, book_id):
    return next((record for record in borrow_records if record["user_id"] == user_id and record["book_id"] == book_id and record["return_date"] is None), None)


# Get all available books
@Borrow_router.get("/books/available", status_code=200)
def get_available_books():
    available_books = [book for book in books if book["is_available"]]
    if not available_books:
        raise HTTPException(status_code=404, detail="No books are currently available.")
    return {"available_books": available_books}


# Borrow a book
@Borrow_router.post("/borrow", status_code=201)
def borrow_book(request: BorrowRequest):
    user = find_user_by_id(request.user_id)
    if not user or not user["is_active"]:
        raise HTTPException(status_code=400, detail="User not found or inactive.")

    book = find_book_by_id(request.book_id)
    if not book or not book["is_available"]:
        raise HTTPException(status_code=400, detail="Book not found or unavailable.")

    if find_active_borrow_record(request.user_id, request.book_id):
        raise HTTPException(status_code=400, detail="User has already borrowed this book.")

    # Borrow the book
    borrow_record = {
        "id": len(borrow_records) + 1,
        "user_id": request.user_id,
        "book_id": request.book_id,
        "borrow_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "return_date": None
    }
    borrow_records.append(borrow_record)
    book["is_available"] = False

    return {"message": "Book successfully borrowed.", "borrow_record": borrow_record}

# Return a book
@Borrow_router.post("/return", status_code=200)
def return_book(request: ReturnRequest):
    borrow_record = find_active_borrow_record(request.user_id, request.book_id)
    if not borrow_record:
        raise HTTPException(status_code=404, detail="No active borrow record found for this user and book.")

    # Return the book
    borrow_record["return_date"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    book = find_book_by_id(request.book_id)
    if book:
        book["is_available"] = True

    return {"message": "Book successfully returned.", "borrow_record": borrow_record}

