from fastapi import FastAPI
from app.Entidades.Categoria.router import router as categoria_router
from app.database import create_db_and_tables
from app.Entidades.Ingrediente.router import router as ingrediente_router
from app.Entidades.Producto.router import router as producto_router



def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 1",
        description="Conceptos: Path, Query, Body, Pydantic, Errores.",
        version="1.0.0"
    )

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()
    
    app.include_router(categoria_router)
    app.include_router(ingrediente_router)
    app.include_router(producto_router)
    
    return app

app = create_app()
