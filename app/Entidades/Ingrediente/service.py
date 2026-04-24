from . import model
from . import schema
from sqlmodel import Session, select
from datetime import datetime


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

