from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
from app.Entidades.TablasIntermedias.ProductoIngrediente.model import ProductoIngrediente
if TYPE_CHECKING:
    from app.Entidades.Producto.model import Producto

class Ingrediente(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(max_length=100, unique=True)
    descripcion: str | None = None
    es_alergeno: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    productos: list["Producto"] = Relationship(
        link_model=ProductoIngrediente,
        back_populates="ingredientes"
    )