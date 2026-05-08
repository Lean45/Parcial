from sqlmodel import SQLModel, Field

class ProductoIngrediente(SQLModel, table=True):
    producto_id: int = Field(default=None, primary_key=True, foreign_key="producto.id")
    ingrediente_id: int = Field(default=None, primary_key=True, foreign_key="ingrediente.id")
    