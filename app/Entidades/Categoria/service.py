from sqlmodel import Session, select
from app.Entidades.Categoria.model import Categoria
from app.Entidades.Categoria.schema import CategoriaCreate, CategoriaUpdate
from datetime import datetime

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


    