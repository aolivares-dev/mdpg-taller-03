from fastapi import APIRouter, HTTPException
from app.database import database
from app.models.specialty import specialty
from app.schemas.specialties import CreateSpecialty, UpdateSpecialty, Specialty
from app.utils.response_messages import ResponseMessage

router = APIRouter(prefix="/specialties_view", tags=["specialties_view"])

@router.get("/", response_model=list[Specialty])
async def list_specialties():
    query = specialty.select()
    return await database.fetch_all(query)

@router.get("/{id}", response_model=Specialty)
async def get_specialty(id: int):
    query = specialty.select().where(specialty.c.id == id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail=ResponseMessage.SPECIALTY_NOT_FOUND.value)
    return result

@router.post("/", response_model=Specialty)
async def create_specialty(specialty_data: CreateSpecialty):
    try:
        query = specialty.insert().values(**specialty_data.model_dump())
        inserted_id = await database.execute(query)
        return {**specialty_data.model_dump(), "id": inserted_id}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_CREATE_SPECIALTY.value)

@router.put("/{id}", response_model=Specialty)
async def update_specialty(id: int, specialty_data: UpdateSpecialty):
    query = specialty.select().where(specialty.c.id == id)
    existing = await database.fetch_one(query)
    if not existing:
        raise HTTPException(status_code=404, detail=ResponseMessage.SPECIALTY_NOT_FOUND.value)
    try:
        update_query = specialty.update().where(specialty.c.id == id).values(**specialty_data.model_dump())
        await database.execute(update_query)
        return {**existing, **specialty_data.model_dump()}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_UPDATE_SPECIALTY.value)

@router.delete("/{id}", response_model=dict)
async def delete_specialty(id: int):
    try:
        delete_query = specialty.delete().where(specialty.c.id == id)
        deleted = await database.execute(delete_query)
        if deleted == 0:
            raise HTTPException(status_code=404, detail=ResponseMessage.SPECIALTY_NOT_FOUND.value)
        return {"message": ResponseMessage.SPECIALTY_DELETED.value}
    except Exception:
        raise HTTPException(status_code=500, detail=ResponseMessage.ERROR_DELETE_SPECIALTY.value)
