from sqlmodel import SQLModel, Field
from datetime import datetime

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
    
    