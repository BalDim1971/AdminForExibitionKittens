from contextlib import asynccontextmanager
from fastapi import FastAPI

from breed.routes import app_kitten
from src.database import create_tables, create_async_engine, delete_tables


@asynccontextmanager
async def connect_db(app: FastAPI):
    await create_tables()
    print('Подключение к БД')
    yield
    await delete_tables()
    print('Подключение к БД завершено')


app = FastAPI(
    title="Выставка котят",
    description="Сервис для управления выставкой котят",
    version="0.1.0",
    docs_url="/",
    openapi_url="/openapi.json",
    lifespan=connect_db,
)

app.include_router(app_kitten)


@app.get("/")
async def home():
    return {"data": "Hello World"}


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(
        "main:app",
        log_level="info",
        reload=True)
