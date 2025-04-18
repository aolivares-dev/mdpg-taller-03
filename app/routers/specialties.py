from fastapi import APIRouter, HTTPException
from app.database import database
from app.models.specialty import specialty
from app.schemas.specialties import CreateSpecialty, UpdateSpecialty, Specialty

router = APIRouter(prefix="/specialties_view", tags=["specialties_view"])

@router.get("/", response_model=list[Specialty])
async def list_specialties_view():
    query = specialty.select()
    return await database.fetch_all(query)

@router.get("/{id}", response_model=Specialty)
async def get_specialty(id: int):
    query = specialty.select().where(specialty.c.id == id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Specialty not found")
    return result

@router.post("/", response_model=Specialty)
async def create_specialty(new_specialty: CreateSpecialty):
    try:
        query = specialty.insert().values(**new_specialty.dict())
        inserted_id = await database.execute(query)
        return {**new_specialty.dict(), "id": inserted_id}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while creating the specialty. Please try again."
        )

@router.delete("/{id}", response_model=dict)
async def delete_specialty(id: int):
    try:
        query = specialty.delete().where(specialty.c.id == id)
        deleted = await database.execute(query)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Specialty not found")
        return {"message": "Specialty deleted successfully"}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="An error occurred while deleting the specialty. Please try again."
        )
