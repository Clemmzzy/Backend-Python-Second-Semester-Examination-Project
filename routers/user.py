from fastapi import APIRouter, HTTPException
from typing import List
from schemas.user import User, users

user_router = APIRouter()

# Get all users
@user_router.get("/users", response_model=List[User], status_code=200)
def get_all_users():
    return users

# Get a specific user
@user_router.get("/{user_id}", response_model=User, status_code=200)
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

# Create a user
@user_router.post("/users", status_code=201)
def create_user(user: User):
    if any(u["id"] == user.id for u in users):
        raise HTTPException(status_code=400, detail="User_ID already exists.")
    users.append(user.model_dump())
    return user

# Update a user
@user_router.put("/{user_id}", response_model=User, status_code=200)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            users[i] = updated_user.model_dump()
            return updated_user
    raise HTTPException(status_code=404, detail="User not found.")

# Delete a user
@user_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted successfully."}

# Deactivate a user
@user_router.patch("/{user_id}/deactivate", status_code=200)
def deactivate_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    user["is_active"] = False
    return {"message": "User deactivated Successfully."}



# @user_router.get("/", status_code=200)
# async def get_all_user():
#     return {"data": {user.values()}, "message": "succesful"}


# @user_router.post("/", status_code=201)
# async def create_user(user_data: usercreate):
#     user = user_crud.create_user(user_data)
#     return {"data": user, "message": "User created successfully"}

# @user_router.get("/{user_id}", status_code=200)
# async def get_user_by_id(user_id: int):
#     user = user_crud.get_user_by_id(user_id)
#     return {"data": user, "message": "successful"}