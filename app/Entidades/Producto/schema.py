from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from sqlalchemy import Numeric, Column

class ProductoBase(SQLModel):
    nombre: str = Field(max_length=150)
    descripcion: Optional[str] = None
    precio_base: float = Field(default=0.0, sa_column=Column(Numeric(10, 2), nullable=False))
    imagenes_url: Optional[list[str]] = None
    stock_cantidad: int = Field(default=0)
    disponible: bool = Field(default=True)

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, max_length=150)
    descripcion: Optional[str] = None
    precio_base: Optional[float] = Field(default=None, sa_column=Column(Numeric(10, 2), nullable=False))
    imagenes_url: Optional[list[str]] = None
    stock_cantidad: Optional[int] = Field(default=None)
    disponible: Optional[bool] = Field(default=None)

class ProductoRead(ProductoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None   
    