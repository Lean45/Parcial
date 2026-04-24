from sqlmodel import Session
from app.database import engine
from app.Entidades.Producto.repository import ProductoRepository


class UnitOfWork:
    def __init__(self):
        self.session_factory = lambda: Session(engine)

    def __enter__(self):
        self.session = self.session_factory()
        self.producto_repository = ProductoRepository(self.session)
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.session.rollback()
        else:
            self.session.commit()
        self.session.close()