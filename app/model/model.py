from pydantic import BaseModel
from typing import Optional
from decimal import *

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    tax: Optional[Decimal] = None
