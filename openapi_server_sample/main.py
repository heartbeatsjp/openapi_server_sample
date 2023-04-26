import random
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    description: str | None
    price: float
    tax: float | None


@app.get("/")
async def root() -> str:
    return "hello world"


@app.get("/item")
async def read_item() -> Item:
    return Item(name="test", description="description", price=10, tax=1)
