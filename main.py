from fastapi import FastAPI
import uvicorn
from user import router as user_router
import subprocess

app = FastAPI()
app.include_router(user_router)


# @app.get("/")
# def root(): return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    subprocess.Popen(["python", "discord_cmd.py"])
