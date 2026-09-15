from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class TransactionCreate(BaseModel):
    description: str = Field(min_length=1, max_length=255)

    amount: Decimal = Field(gt=0)

    type: Literal["income", "expense"]

    category_id: int


class TransactionUpdate(BaseModel):
    description: str | None = Field(default=None, min_length=1, max_length=255)

    amount: Decimal | None = Field(default=None, gt=0)

    type: Literal["income", "expense"] | None = None

    category_id: int | None = None


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    description: str
    amount: Decimal
    type: Literal["income", "expense"]
    category_id: int
    user_id: int
    created_at: datetime
