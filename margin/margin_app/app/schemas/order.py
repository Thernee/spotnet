"""
Pydantic schemas for user_order operations.
"""

import uuid
from decimal import Decimal
from typing import Optional

from app.models.user_order import UserOrder
from .base import GetAll
from pydantic import BaseModel, Field, ConfigDict


class UserOrderCreate(BaseModel):
    """Schema for creating a new order"""

    user_id: uuid.UUID = Field(..., description="ID of the user placing the order")
    price: Decimal = Field(..., description="Price of the order")
    token: str = Field(..., description="Token symbol for the order")
    position: uuid.UUID = Field(..., description="Position ID related to the order")


class UserOrderResponse(BaseModel):
    """Schema for order response"""

    id: uuid.UUID
    user_id: uuid.UUID
    price: Decimal
    token: str
    position: uuid.UUID

    class Config:
        """Pydantic model configuration"""

        from_attributes = True


class UserOrderGetAllResponse(GetAll[UserOrderResponse]):
    """Schema retrieving all users"""


class UserOrderUpdate(BaseModel):
    """Schema for updating an order."""
    model_config = ConfigDict(
        json_encoders={
            uuid.UUID: str,
            Decimal: str,
        }
    )
    
    user_id: Optional[uuid.UUID] = None
    price: Optional[Decimal] = None
    token: Optional[str] = None
    position: Optional[uuid.UUID] = None