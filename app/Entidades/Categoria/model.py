from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from app.Entidades.TablasIntermedias.ProductoCategoria.model import ProductoCategoria

if TYPE_CHECKING:
    from app.Entidades.Producto.model import Producto
class Categoria(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    parent_id: int | None = Field(default=None, foreign_key="categoria.id")
    nombre: str = Field(max_length=100, unique=True)
    descripcion: str | None = None
    imagen_url: str | None = None
    disponible: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: datetime | None = None

    productos: list["Producto"] = Relationship(
        link_model=ProductoCategoria,
        back_populates="categorias"
    )
    
    subcategorias: list["Categoria"] = Relationship(
        sa_relationship_kwargs={
            "primaryjoin": "Categoria.id == foreign(Categoria.parent_id)",
            "lazy": "selectin"
        }
    )
    