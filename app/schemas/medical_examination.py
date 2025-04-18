# app/schemas/vista_medico.py

from pydantic import BaseModel

class MedicalExamination(BaseModel):
    id: int
    name: str
    lastname: str
    specialties: str

    class Config:
        from_attributes = True
