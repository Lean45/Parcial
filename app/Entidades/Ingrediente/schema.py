from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class IngredienteBase(SQLModel):
    nombre: str = Field(max_length=100, unique=True)
    descripcion: Optional[str] = None
    es_alergeno: bool = Field(default=False)
    

class IngredienteCreate(IngredienteBase):
    pass
    

class IngredienteUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, max_length=100)
    descripcion: Optional[str] = None
    es_alergeno: Optional[bool] = None
    
class IngredienteRead(IngredienteBase):
    id: int
    created_at: datetime
    updated_at: datetime