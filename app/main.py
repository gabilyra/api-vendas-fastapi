#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/")
#def read_root():
#return {"message": "API funcionando!"}

from fastapi import FastAPI
from app.database.database import engine

app = FastAPI()

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