from fastapi import FastAPI
from app.database import engine
from app.routers import cliente

app = FastAPI()

app.include_router(cliente.router)

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            return {"message": "Conexão com banco OK!"}
    except Exception as e:
        return {"error": str(e)}