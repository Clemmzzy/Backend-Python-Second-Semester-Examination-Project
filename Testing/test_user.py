# from fastapi.testclient import TestClient
# from routers.user import user_router

# client = TestClient(user_router)

# test_users = [
#     {"id": 1, "Name": "John Doe", "email": "john.doe@example.com", "is_active": True},
#     {"id": 2, "Name": "Caleb Stone", "email": "Caleb.stone@example.com", "is_active": True},
# ]
# test_books = [
#     {"id": 1, "Title": "The Rising Sun", "author": "Clement Ugwu", "is_available": True},
#     {"id": 2, "Title": "Purle Hibiscus", "author": "Chimamanda Adichie", "is_available": True},
# ]


# user = [test_users]
# Book = [test_books]
# borrow_records = []


# def test_get_all_users():
#     response = client.get("/users/")
#     assert response.status_code == 200


# def test_create_user(reset_data):
#     new_user = {"id": 2, "name": "Jane Doe", "is_active": True}
#     response = client.post("/users/", json=new_user)
#     assert response.status_code == 201
#     assert response.json() == new_user


# def test_update_user(reset_data):
#     updated_user = {"id": 1, "name": "John Updated", "is_active": True}
#     response = client.put(f"/users/{test_users['id']}", json=updated_user)
#     assert response.status_code == 200
#     assert response.json() == updated_user


# def test_delete_user(reset_data):
#     response = client.delete(f"/users/{test_users['id']}")
#     assert response.status_code == 204


# def test_deactivate_user(reset_data):
#     response = client.patch(f"/users/{test_users['id']}/deactivate")
#     assert response.status_code == 200
#     assert response.json()["message"] == "User deactivated Successfully."


# def test_get_all_books(reset_data):
#     response = client.get("/books/")
#     assert response.status_code == 200
#     assert response.json() == Book