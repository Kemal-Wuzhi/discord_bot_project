import os
from fastapi import FastAPI, APIRouter
import threading
import dotenv
from dao import UserDatabase
from discord import Client
from discord.utils import oauth_url
from discord import Permissions
from discord_cmd import bot


db = UserDatabase('users.db')
users = []
router = APIRouter()

dotenv.load_dotenv("./env/local.env")
bot_token = os.getenv("DISCORD_BOT_TOKEN")


def run_bot():
    bot.run(bot_token)


bot_thread = threading.Thread(target=run_bot)
bot_thread.start()


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
    user = db.get_user(username)
    if user is None:
        return {"message": "User not found"}
    db.delete_user(username)
    return {"message": "User deleted successfully"}


@router.get("/invite")
async def get_invite_link():
    if bot.user is None:
        return {"message": "Bot is not connected"}
    permissions = Permissions(permissions=8)  # Use the permissions you need
    invite_link = oauth_url(bot.user.id, permissions=permissions)
    return {"invite_link": invite_link}
