from fastapi import FastAPI, APIRouter
from dao import UserDatabase
app = FastAPI()

db = UserDatabase('users.db')
users = []
router = APIRouter()


@router.post("/register")
def register(username: str, password: str):
    user = {"username": username, "password": password}
    users.append(user)
    db.register(username, password)  # Call register on the instance
    return {"message": "User registered successfully"}


@router.post("/login")
def login(username: str, password: str):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"message": "Login successful"}
    return {"message": "Invalid username or password"}


@router.delete("/delete")
def delete(username: str):
    for user in users:
        if user["username"] == username:
            users.remove(user)
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}
