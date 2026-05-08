from sqlmodel import SQLModel, Field, Column, ARRAY, TEXT, Relationship
from datetime import datetime
from sqlalchemy import Numeric
from app.Entidades.TablasIntermedias.ProductoCategoria.model import ProductoCategoria
from app.Entidades.Categoria.model import Categoria
from app.Entidades.TablasIntermedias.ProductoIngrediente.model import ProductoIngrediente
from app.Entidades.Ingrediente.model import Ingrediente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.Entidades.Categoria.model import Categoria
    from app.Entidades.Ingrediente.model import Ingrediente

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=150, unique=True)
    descripcion: str | None = None
    precio_base: float = Field(default=0.0, ge=0, sa_column=Column(Numeric(10, 2), nullable=False))
    imagenes_url: list[str] | None = Field(default=None, sa_column=Column(ARRAY(TEXT)))
    stock_cantidad: int = Field(default=0)
    disponible: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None

    categorias: list["Categoria"] = Relationship(
        link_model=ProductoCategoria,
        back_populates="productos"
    )

    ingredientes: list["Ingrediente"] = Relationship(
        link_model=ProductoIngrediente,
        back_populates="productos"
    )