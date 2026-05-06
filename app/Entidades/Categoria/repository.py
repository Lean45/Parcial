from sqlmodel import Session
from app.database import engine
from app.Entidades.Core.BaseRepository import BaseRepository
from app.Entidades.Categoria.model import Categoria

class CategoriaRepository(BaseRepository[Categoria]):
    def __init__(self, session: Session):
        super().__init__(session, Categoria)
