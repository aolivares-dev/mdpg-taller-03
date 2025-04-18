from typing import Optional
from pydantic import BaseModel

class BasicMedicalExamination(BaseModel):
    id: Optional[int] = None
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
