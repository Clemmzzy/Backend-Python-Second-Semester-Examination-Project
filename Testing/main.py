from fastapi import FastAPI
from fastapi.testclient import TestClient
from routers.user import user_router

client = TestClient(user_router)