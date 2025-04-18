# app/schemas/vista_medico.py

from pydantic import BaseModel

class BasicMedicalExamination(BaseModel):
    id: int
    name: str
    lastname: str
    specialties: str
    
class CreateMedicalExamination(BasicMedicalExamination):
    pass

class UpdateMedicalExamination(BasicMedicalExamination):
    pass

class MedicalExamination(BasicMedicalExamination):
    id: int

    class Config:
        from_attributes = True
