from sqlmodel import Session
from app.database import engine
from app.Entidades.Core.BaseRepository import BaseRepository
from app.Entidades.Producto.model import Producto

class ProductoRepository(BaseRepository[Producto]):
    def __init__(self, session: Session):
        super().__init__(session, Producto)
