from . import model
from . import schema
from sqlmodel import Session, select
from datetime import datetime
from app.Entidades.Ingrediente.repository import IngredienteRepository
from app.Entidades.Core.uow import UnitOfWork
from typing import List

def  crear_ingrediente(datos: schema.IngredienteCreate) -> schema.IngredienteRead | None:
    with UnitOfWork() as uow:
        ingrediente = uow.ingrediente_repository.create(datos)
        result = schema.IngredienteRead.model_validate(ingrediente)
        return result

def obtener_ingrediente_por_id(id: int) -> schema.IngredienteRead | None:
    with UnitOfWork() as uow:
        ingrediente = uow.ingrediente_repository.get_by_id(id)
        if not ingrediente:
            raise ValueError("Ingredinte no encontrado")
        return schema.IngredienteRead.model_validate(ingrediente)

def obtener_todos_los_ingredientes() -> List[schema.IngredienteRead]:
    with UnitOfWork() as uow:
        ingrediente = uow.ingrediente_repository.get_all()
        return [schema.IngredienteRead.model_validate(p) for p in ingrediente]

def actualizar_ingrediente(id: int, datos: schema.IngredienteUpdate) -> schema.IngredienteRead | None:
    with UnitOfWork() as uow:
        ingrediente = uow.ingrediente_repository.update(id, datos)
        return schema.IngredienteRead.model_validate(ingrediente)

def borrado_soft_ingrediente(id: int):
    with UnitOfWork() as uow:
        ingrediente = uow.ingrediente_repository.delete(id)
        return schema.IngredienteRead.model_validate(ingrediente)




"""
def Crear_ingrediente(datos: schema.IngredienteCreate, session: Session) -> model.Ingrediente:
    ingrediente = model.Ingrediente.model_validate(datos)
    session.add(ingrediente)
    session.commit()
    session.refresh(ingrediente)
    return ingrediente

def Obtener_ingrediente_por_id(id: int, session: Session) -> model.Ingrediente:
    ingrediente = session.get(model.Ingrediente, id)
    if not ingrediente:
        raise ValueError("Ingrediente no encontrado")
    return ingrediente

def Obtener_todos_los_ingredientes(session: Session) -> list[model.Ingrediente]:
    statement = select(model.Ingrediente)
    ingredientes = session.exec(statement).all()
    return ingredientes

def Actualizar_ingrediente(id: int, datos: schema.IngredienteUpdate, session: Session) -> model.Ingrediente:
    ingrediente = session.get(model.Ingrediente, id)
    if not ingrediente:
        raise ValueError("Ingrediente no encontrado")
    update_data = datos.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(ingrediente, key, value)
    ingrediente.updated_at = datetime.now()
    session.add(ingrediente)
    session.commit()
    session.refresh(ingrediente)
    return ingrediente

"""