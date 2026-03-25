from fastapi import FastAPI
from .routes.users import users_router

app = FastAPI(
    title="DSFRTech Formations FastAPI introduction",
    version="1.0.0",
    description="A simple FastAPI application to demonstrate the basics of FastAPI.",
)


@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World!"}


@app.get("/health", status_code=200)
async def health():
    return {"status": "ok"}


app.include_router(users_router)
