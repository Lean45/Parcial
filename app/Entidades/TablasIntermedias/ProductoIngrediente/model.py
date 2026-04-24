from sqlmodel import SQLModel, Field

def ProductoIngrediente(SQLModel, table=True):
    producto_id: int = Field(default=None, primary_key=True, foreign_key="producto.id")
    ingrediente_id: int = Field(default=None, primary_key=True, foreign_key="ingrediente.id")
    es_removible: bool = Field(default=False)
    