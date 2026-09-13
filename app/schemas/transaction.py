from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field

class TransactionCreate(BaseModel):
    description: str = Field(min_lenght=1, max_length=255)
    amount: Decimal = Field(gt=0)
    type: Literal["income", "expense"]
    category_id: int

class TransactionUpdate(BaseModel):
     description: str | None = Field(
          default=None,
          min_length=1,
          max_length=255
     )

     amount: Decimal | None = Field(
          default=None,
          gt=0
     )

     type: Literal["income", "expense"] | None = None

     category_id: int | None = None

class TransactionResponse(BaseModel):
    id: int
    description: str
    amount: Decimal
    type: Literal["income", "expense"]
    category_id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
    
