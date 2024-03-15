from sqlmodel import Field, SQLModel, Relationship
from typing import Optional
from decimal import Decimal


class Product(SQLModel, table=True):
    # NOTE: https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/?h=required#so-why-is-it-important-to-have-required-ids
    id: Optional[int] = Field(default=None, primary_key=True)

    # NOTE: Unique identifier in provider (i.e. AWS, GCP, Azure etc.)
    sku: str = Field(max_length=255, unique=True, index=True)

    provider: str = Field(max_length=100)
    machine_name: str = Field(max_length=255)
    value: Decimal = Field(default=0, max_digits=5, decimal_places=3)
    cpu: int = Field(default=0)
    ram: int = Field(default=0)
    disk: int = Field(default=0)


class SnapshotProduct(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: Optional[int] = Field(foreign_key="product.id")
    snapshot: str
