# app/schemas/especialidad.py

from pydantic import BaseModel

class BasicSpecialty(BaseModel):
    name: str
    description: str | None = None

class CreateSpecialty(BasicSpecialty):
    pass

class UpdateSpecialty(BasicSpecialty):
    pass

class Specialty(BasicSpecialty):
    id: int

    class Config:
        from_attributes = True
