from . import model
from . import schema
from sqlmodel import Session, select
from datetime import datetime
from app.Entidades.Core.uow import UnitOfWork
from app.Entidades.Producto.model import Producto
"""
def create_producto(data: schema.ProductoCreate) -> schema.ProductoRead:
    with UnitOfWork() as uow:
        uow.producto_repository.create(data)
        result = schema.ProductoRead.model_validate(data)
        return result
"""
def create_producto(data: schema.ProductoCreate) -> schema.ProductoRead:
    with UnitOfWork() as uow:
        producto = uow.producto_repository.create(data)
        result = schema.ProductoRead.model_validate(producto)
        return result


def get_producto_by_id(id: int, uow: UnitOfWork) -> schema.ProductoRead:
    with UnitOfWork() as uow:
        producto = uow.producto_repository.get_by_id(id)
        if not producto:
            raise ValueError("Producto no encontrado")
        return schema.ProductoRead.model_validate(producto)

def get_all_productos() -> list[schema.ProductoRead]:
    with UnitOfWork() as uow:
        productos = uow.producto_repository.get_all()
        return [schema.ProductoRead.model_validate(p) for p in productos]

def Actualizar_Producto(id: int, data: schema.ProductoUpdate) -> schema.ProductoRead:
    with UnitOfWork() as uow:
        producto = uow.producto_repository.update(id, data)
        if not producto:
            raise ValueError("Producto no encontrado")

        return schema.ProductoRead.model_validate(producto)

def Borrado_Soft_Producto(id: int) -> model.Producto:
    with UnitOfWork() as uow:
        producto = uow.producto_repository.delete(id)
        return schema.ProductoRead.model_validate(producto)

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