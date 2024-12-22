from fastapi import APIRouter, HTTPException
from schemas.BorrowRecord import borrow_records
from routers.BorrowRecord import find_user_by_id


Borrow_Management = APIRouter()


# Get borrowing records for a specific user
@Borrow_Management.get("/records/user/{user_id}", status_code=200)
def get_user_borrow_records(user_id: int):
    user = find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    user_records = [record for record in borrow_records if record["user_id"] == user_id]
    if not user_records:
        raise HTTPException(status_code=404, detail="No borrowing records found for this user.")

    return {"user_id": user_id, "borrow_records": user_records}

# Get all borrowing records
@Borrow_Management.get("/records", status_code=200)
def get_all_borrow_records():
    if not borrow_records:
        raise HTTPException(status_code=404, detail="No borrowing records found.")
    return {"borrow_records": borrow_records}