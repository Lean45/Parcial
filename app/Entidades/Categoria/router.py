from fastapi import APIRouter, Depends, HTTPException
from app.Entidades.Categoria.schema import CategoriaCreate, CategoriaRead, CategoriaUpdate
from . import service
from app.database import get_session
from sqlmodel import Session

router = APIRouter(prefix="/categorias", tags=["Categorías"])

@router.post("/", response_model=CategoriaRead)
def crear_categoria(datos: CategoriaCreate, session: Session = Depends(get_session)):
    try:
        return service.crear_categoria(datos, session)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{id}", response_model=CategoriaRead)
def borrado_soft_categoria(id: int, session: Session = Depends(get_session)):
    try:
        return service.borrado_soft_categoria(id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{id}", response_model=CategoriaRead)
def actualizar_categoria(id: int, datos: CategoriaUpdate, session: Session = Depends(get_session)):
    try:
        return service.actualizar_categoria(id, datos, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[CategoriaRead])
def obtener_todas_categorias(session: Session = Depends(get_session)):
    return service.Obtener_todas_categorias(session)

@router.get("/{id}", response_model=CategoriaRead)
def obtener_categoria_por_id(id: int, session: Session = Depends(get_session)):
    try:
        return service.obtener_categoria_por_id(id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/subcategorias/{id}", response_model=list[CategoriaRead])
def obtener_subcategorias(id: int, session: Session = Depends(get_session)):
    try:
        return service.obtener_subcategorias(id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))