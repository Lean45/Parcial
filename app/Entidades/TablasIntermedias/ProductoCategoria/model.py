from sqlmodel import SQLModel, Field, Relationship


class ProductoCategoria(SQLModel, table=True):
    producto_id: int = Field(default=None, primary_key=True, foreign_key="producto.id")
    categoria_id: int = Field(default=None, primary_key=True, foreign_key="categoria.id")