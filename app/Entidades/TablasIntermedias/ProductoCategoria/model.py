from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime


class ProductoCategoria(SQLModel, table=True):
    producto_id: int = Field(default=None, primary_key=True, foreign_key="producto.id")
    categoria_id: int = Field(default=None, primary_key=True, foreign_key="categoria.id")
    es_principal: bool = Field(default=False)
    created_at: datetime = Field(default=datetime.now())

    
    