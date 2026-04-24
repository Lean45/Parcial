from fastapi import APIRouter, Depends, HTTPException
from . import service
from . import schema
from app.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/ingredientes", tags=["Ingredientes"])

@router.post("/", response_model=schema.IngredienteRead)
def crear_ingrediente(datos: schema.IngredienteCreate, session: Session = Depends(get_session)):
    try:
        return service.Crear_ingrediente(datos, session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schema.IngredienteRead])
def obtener_todos_los_ingredientes(session: Session = Depends(get_session)):
    return service.Obtener_todos_los_ingredientes(session)

@router.get("/{id}", response_model=schema.IngredienteRead)
def obtener_ingrediente_por_id(id: int, session: Session = Depends(get_session)):
    try:
        return service.Obtener_ingrediente_por_id(id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{id}", response_model=schema.IngredienteRead)
def actualizar_ingrediente(id: int, datos: schema.IngredienteUpdate, session: Session = Depends(get_session)):
    try:
        return service.Actualizar_ingrediente(id, datos, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
