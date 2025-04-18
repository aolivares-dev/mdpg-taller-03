# app/routers/vista_medico.py

from fastapi import APIRouter, HTTPException
from app.database import database
from app.models.medical_examination import medical_examination
from app.schemas.medical_examination import MedicalExamination

router = APIRouter(prefix="/lista-medicos", tags=["lista-medicos"])

@router.get("/", response_model=list[MedicalExamination])
async def listar_vista_medico():
    query = medical_examination.select()
    return await database.fetch_all(query)
