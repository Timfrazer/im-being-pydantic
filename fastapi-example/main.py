from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Tesla(BaseModel):
    name: Optional[str]
    price: Optional[float]
    quantity: int = 0


def make_order(tesla: Tesla):
    # Business logic for creating a Tesla
    return {"tesla": tesla}


@app.get("/")
async def index():
    return {"index": "hi this is the index"}


@app.post("/order/tesla")
async def order_tesla(tesla: Tesla):
    order = make_order(tesla)
    return order


@app.get("/track/{tesla_id}")
def get_order(tesla_id: int, q: Optional[str] = None):
    return {"tesla_id": tesla_id, "q": q}
