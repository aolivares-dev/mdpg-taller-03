# main.py

from fastapi import FastAPI
from app.database import database,  engine, metadata
from app.routers import medical_examination, specialties
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    
    await database.connect()
    yield
    await database.disconnect()

metadata.create_all(bind=engine)
app = FastAPI(lifespan=lifespan)

# Crear tablas (solo una vez, o con checkfirst=True)

app.include_router(specialties.router)
app.include_router(medical_examination.router)
