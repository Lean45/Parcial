from sqlmodel import Session
from app.database import engine
from app.Entidades.Core.BaseRepository import BaseRepository
from app.Entidades.Ingrediente.model import Ingrediente

class IngredienteRepository(BaseRepository[Ingrediente]):
    def __init__(self, session: Session):
        super().__init__(session, Ingrediente)