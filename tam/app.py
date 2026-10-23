from contextlib import asynccontextmanager

from fastapi import FastAPI

from tam.core.database import init_db
from tam.identidade.routers import auth, usuarios


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth.router)
app.include_router(usuarios.router)
