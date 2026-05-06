from fastapi import APIRouter, Depends, HTTPException
from . import service
from . import schema
from app.database import get_session
from sqlmodel import Session


router = APIRouter(prefix="/productos", tags=["Productos"])

@router.post("/", response_model=schema.ProductoRead)
def create_producto(datos: schema.ProductoCreate):
    return service.create_producto(datos)



@router.get("/", response_model=list[schema.ProductoRead])
def obtener_todos_los_productos():
    return service.get_all_productos()

    


@router.get("/{id}", response_model=schema.ProductoRead)
def obtener_producto_por_id(id: int, session: Session = Depends(get_session)):
    try:
        return service.get_producto_by_id(id, session)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))




@router.put("/{id}", response_model=schema.ProductoRead)
def actualizar_producto(id: int, datos: schema.ProductoUpdate, session: Session = Depends(get_session)):
    try:
        return service.Actualizar_Producto(id, datos)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))




@router.delete("/soft/{id}", response_model=schema.ProductoRead)
def borrado_soft_producto(id: int, session: Session = Depends(get_session)):
    try:
        return service.Borrado_Soft_Producto(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
