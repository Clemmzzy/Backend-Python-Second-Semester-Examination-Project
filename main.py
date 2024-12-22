from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
from routers.user import user_router
from routers.Book import Book_router
from routers.BorrowRecord import Borrow_router
from routers.Borrow_Management import Borrow_Management
from pydantic import BaseModel

app = FastAPI(
    title="E Library API System | Clement Ugwu | ALT/SOE/024/0106",
    description="Backend Python Second Semester Examination Project",
)

@app.get("/", status_code=200)
def home():
    return "Welcome to Clement Ugwu E-Library API System | ALT/SOE/024/0106 ", "Backend Python Second Semester Examination Project"


app.include_router(user_router, prefix="/user", tags=["Users"])
app.include_router(Book_router, prefix="/Book", tags=["Books"])
app.include_router(Borrow_router, prefix="/BorrowRecord", tags=["Borrow Operations"])
app.include_router(Borrow_Management, prefix="/BorrowManagement", tags=["Borrow Records Management"])