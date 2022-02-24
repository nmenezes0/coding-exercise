from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def hello_world():
    return "Hello World"


@app.get("/add/")
async def add_two_numbers(first: int = 0, second: int = 0):
    return first + second


@app.get("/joinstrings/")
async def join_strings(first_str: str = "", second_str: str = ""):
    return f"{first_str}-{second_str}"
