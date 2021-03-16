from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from typing import Tuple, Optional
from enum import Enum


app = FastAPI()

class Battery(str, Enum):
 standard = 'standard'
 long_range = 'long range'


class TeslaCarModels(str, Enum):
    pass

class Tesla(BaseModel):
 style: str
 battery_pack: Tuple[Battery, ...]
 insane_mode: Optional[bool] = None



def make_order(tesla: Tesla):
    # Business logic for creating a Tesla
    return {'tesla': tesla}

@app.post("/order/tesla")
async def order_tesla(tesla: Tesla):
    order = make_order(tesla)
    return order