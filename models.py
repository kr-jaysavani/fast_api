
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

   
# from pydantic import BaseModel, Field


# class Product(BaseModel):
#     id: int = Field(..., gt=0, description="Product ID must be positive")
#     name: str = Field(..., min_length=1, max_length=100, description="Product name")
#     description: str = Field(..., min_length=10, max_length=500, description="Product description")
#     price: float = Field(..., gt=0, le=10000, description="Price must be positive and <= 10000")
#     quantity: int = Field(..., ge=0, le=10000, description="Quantity must be non-negative")