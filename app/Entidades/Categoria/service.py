from sqlmodel import Session, select
from . import model
from . import schema
from datetime import datetime
from app.Entidades.Categoria.repository import CategoriaRepository
from app.Entidades.Core.uow import UnitOfWork

def crear_categoria(data: schema.CategoriaCreate) -> schema.CategoriaRead | None:
    with UnitOfWork() as uow:
        categoria = uow.categoria_repository.create(data)
        result = schema.CategoriaRead.model_validate(categoria)
        return result

def obtener_categoria_por_id(id: int) -> schema.CategoriaRead:
    with UnitOfWork() as uow:
        categorias = uow.categoria_repository.get_by_id(id)
        if not categorias:
            raise ValueError("Categoria no encontrada")
        return schema.CategoriaRead.model_validate(categorias)

def Obtener_todas_categorias() -> List[schema.CategoriaRead]:
    with UnitOfWork() as uow:
        categorias = uow.categoria_repository.get_all()
        return [schema.CategoriaRead.model_validate(p) for p in categorias]

def actualizar_categoria(id: int, data: schema.CategoriaUpdate) -> schema.CategoriaRead:
    with UnitOfWork() as uow:
        update_data = uow.categoria_repository.update(id, data)
        return schema.CategoriaRead.model_validate(update_data)

def borrado_soft_categoria(id: int):
    with UnitOfWork() as uow:
        borrado = uow.categoria_repository.delete(id)
        return schema.CategoriaRead.model_validate(borrado)


"""
def crear_categoria(datos: CategoriaCreate, session: Session) -> Categoria:
    categoria = Categoria.model_validate(datos)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def borrado_soft_categoria(id: int, session: Session) -> Categoria:
    categoria = session.get(Categoria, id)
    if not categoria:
        raise ValueError("Categoria no encontrada")
    if categoria.deleted_at:
        raise ValueError("Categoria ya eliminada")
    categoria.disponible = False
    categoria.deleted_at = datetime.now()
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def actualizar_categoria(id: int, datos: CategoriaUpdate, session: Session) -> Categoria:
    categoria = session.get(Categoria, id)
    if not categoria:
        raise ValueError("Categoria no encontrada")
    if categoria.deleted_at:
        raise ValueError("Categoria eliminada")
    update_data = datos.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(categoria, key, value)
    categoria.updated_at = datetime.now()
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def Obtener_todas_categorias(session: Session) -> list[Categoria]:
    statement = select(Categoria)
    categorias = session.exec(statement).all()
    return categorias

def obtener_categoria_por_id(id: int, session: Session) -> Categoria:
    categoria = session.get(Categoria, id)
    if not categoria:
        raise ValueError("Categoria no encontrada")
    return categoria

def obtener_subcategorias(id: int, session: Session) -> list[Categoria]:
    statement = select(Categoria).where(Categoria.parent_id == id)
    subcategorias = session.exec(statement).all()
    return subcategorias
"""

    