from typing import TypeVar, Generic, Type
from sqlmodel import SQLModel, Session,  select
from datetime import datetime

T = TypeVar('T', bound=SQLModel)

class BaseRepository(Generic[T]):
    def __init__(self, session: Session, model: Type[T]):
        self.session = session
        self.model = model

    def create(self, data: T) -> T:
        entity = self.model.model_validate(data)
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        self.session.add(entity)
        self.session.flush()
        self.session.refresh(entity)
        return entity

    def get_by_id(self, id: int) -> T | None:
        return self.session.get(self.model, id)

    #def get_all(self) -> list[T]:
    #    return self.session.exec(select(self.model)).all()

    def get_all(self) -> list[T]:
        entities = self.session.exec(select(self.model)).all()
        return entities

    def update(self, id: int, data: T) -> T:
        entity = self.get_by_id(id)
        if not entity:
            raise ValueError("Entity not found")
        update_data = data.model_dump(exclude_unset=True)
        for x, y in update_data.items():
            setattr(entity, x, y)
        entity.updated_at = datetime.now()
        self.session.add(entity)
        return entity

    def delete(self, id: int) -> T:
        entity = self.get_by_id(id)
        if not entity:
            raise ValueError("Entity not found")
        entity.disponible = False
        entity.deleted_at = datetime.now()
        entity.updated_at = datetime.now()
        self.session.add(entity)
        return entity