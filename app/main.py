from fastapi import FastAPI
from app.routes import api
from app.database import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield  


app = FastAPI(title="Async Document Q&A", lifespan=lifespan)

app.include_router(api.router)
