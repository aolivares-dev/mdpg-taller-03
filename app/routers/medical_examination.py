from fastapi import APIRouter, HTTPException
from app.database import database
from app.models.medical_examination import medical_examination
from app.schemas.medical_examination import (
    BasicMedicalExamination, CreateMedicalExamination, UpdateMedicalExamination
)
from app.utils.response_messages import ResponseMessage

router = APIRouter(prefix="/medical_examination_view", tags=["medical_examination_view"])

@router.get("/", response_model=list[BasicMedicalExamination])
async def list_medical_examinations():
    query = medical_examination.select()
    return await database.fetch_all(query)

@router.get("/{id}", response_model=BasicMedicalExamination)
async def get_medical_examination(id: int):
    query = medical_examination.select().where(medical_examination.c.id == id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail=ResponseMessage.NOT_FOUND.value)
    return result

@router.post("/", response_model=BasicMedicalExamination)
async def create_medical_examination(exam: CreateMedicalExamination):
    try:
        query = medical_examination.insert().values(**exam.model_dump())
        inserted_id = await database.execute(query)
        return {**exam.model_dump(), "id": inserted_id}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_CREATE.value)

@router.put("/{id}", response_model=BasicMedicalExamination)
async def update_medical_examination(id: int, exam: UpdateMedicalExamination):
    query = medical_examination.select().where(medical_examination.c.id == id)
    existing = await database.fetch_one(query)
    if not existing:
        raise HTTPException(status_code=404, detail=ResponseMessage.NOT_FOUND.value)
    try:
        update_query = medical_examination.update().where(medical_examination.c.id == id).values(**exam.model_dump())
        await database.execute(update_query)
        return {**existing, **exam.model_dump()}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_UPDATE.value)

@router.delete("/{id}", response_model=dict)
async def delete_medical_examination(id: int):
    try:
        delete_query = medical_examination.delete().where(medical_examination.c.id == id)
        deleted = await database.execute(delete_query)
        if deleted == 0:
            raise HTTPException(status_code=404, detail=ResponseMessage.NOT_FOUND.value)
        return {"message": ResponseMessage.DELETED.value}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_DELETE.value)
