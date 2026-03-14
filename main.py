from fastapi import FastAPI

app = FastAPI()


@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World!"}


@app.get("/health", status_code=200)
async def health():
    return {"status": "ok"}


@app.get("/users", status_code=200)
async def get_users():
    return {"data": ["Hugo", "Leozao", "Mariana"]}


# Path parameters
@app.get("/users/{userId}", status_code=200)
async def get_user_by_id(userId: int):
    return {"userId": userId, "message": f"User {userId}"}


# Path parameters
@app.get("/users/name/{userName}", status_code=200)
async def get_user_by_name(userName: str):
    return {"userName": userName, "message": f"User {userName}"}


# Path parameters
@app.get("/sum/{a}/{b}", status_code=200)
async def sum_numbers(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}


# Query parameters
@app.get("/profile", status_code=200)
async def get_profile(name: str, age: int):
    return {"message": f"{name} tem {age} anos."}
