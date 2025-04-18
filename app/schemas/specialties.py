from typing import Optional
from pydantic import BaseModel

class BasicSpecialty(BaseModel):
    id: Optional[int] = None
    name: str
    description: str | None = None

class CreateSpecialty(BasicSpecialty):
    pass

class UpdateSpecialty(BasicSpecialty):
    pass

class Specialty(BasicSpecialty):
    id: Optional[int] = None

    class Config:
        from_attributes = True
