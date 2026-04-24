from . import model
from . import schema
from sqlmodel import Session, select
from datetime import datetime
from app.Entidades.Core.uow import UnitOfWork
from app.Entidades.Producto.model import Producto

def create_producto(data: schema.ProductoCreate) -> model.Producto:
    with UnitOfWork() as uow:
        producto = Producto.model_validate(data)
        return uow.producto_repository.create(producto)

def get_producto_by_id(id: int, uow: UnitOfWork) -> model.Producto:
    with uow:
        return uow.producto_repository.get_by_id(id)

def get_all_productos(uow: UnitOfWork) -> list[model.Producto]:
    with uow:
        return uow.producto_repository.get_all()

def update_producto(id: int, data: schema.ProductoUpdate, uow: UnitOfWork) -> model.Producto:
    with uow:
        return uow.producto_repository.update(id, data)

def delete_producto(id: int, uow: UnitOfWork) -> model.Producto:
    with uow:
        return uow.producto_repository.delete(id)

"""
def Create_producto(data: schema.ProductoCreate, session: Session) -> model.Producto:
    producto = model.Producto.model_validate(data)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

def Obtener_Producto_Por_Id(id: int, session: Session) -> model.Producto:
    producto = session.get(model.Producto, id)
    if not producto:
        raise ValueError("Producto no encontrado")
    return producto

def Obtener_Todos_Los_Productos(session: Session) -> list[model.Producto]:
    statement = select(model.Producto)
    productos = session.exec(statement).all()
    return productos

def Actualizar_Producto(id: int, data: schema.ProductoUpdate, session: Session) -> model.Producto:
    producto = session.get(model.Producto, id)
    if not producto:
        raise ValueError("Producto no encontrado")
    update_data = data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(producto, key, value)
    producto.updated_at = datetime.now()
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

def Borrado_Soft_Producto(id: int, session: Session) -> model.Producto:
    producto = session.get(model.Producto, id)
    if not producto:
        raise ValueError("Producto no encontrado")
    if producto.deleted_at:
        raise ValueError("Producto ya eliminado")
    producto.disponible = False
    producto.deleted_at = datetime.now()
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto

"""