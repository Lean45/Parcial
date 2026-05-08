from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class CategoriaBase(SQLModel):
    
    nombre: str = Field(max_length=100, unique=True)
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None
    

class CategoriaCreate(CategoriaBase):
    parent_id: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.now)
    

class CategoriaUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, max_length=100)
    descripcion: Optional[str] = None
    imagen_url: Optional[str] = None
    parent_id: Optional[int] = None
    updated_at: datetime = Field(default_factory=datetime.now)

class CategoriaRead(CategoriaBase):
    id: int
    parent_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    disponible: bool = Field(default=True)
    subcategorias: list["CategoriaRead"] = []

CategoriaRead.model_rebuild()
