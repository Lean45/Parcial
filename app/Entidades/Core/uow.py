from sqlmodel import Session
from app.database import engine
from app.Entidades.Producto.repository import ProductoRepository
from app.Entidades.Categoria.repository import CategoriaRepository
from app.Entidades.Ingrediente.repository import IngredienteRepository


class UnitOfWork:
    def __init__(self):
        self.session_factory = lambda: Session(engine)

    def __enter__(self):
        self.session = self.session_factory()
        self.producto_repository = ProductoRepository(self.session)
        self.categoria_repository = CategoriaRepository(self.session)
        self.ingrediente_repository = IngredienteRepository(self.session)
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()