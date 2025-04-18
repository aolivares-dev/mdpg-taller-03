# app/models/vista_medico.py

from sqlalchemy import Table, Column, Integer, String
from app.database import metadata

# Definir la vista para los médicos
medical_examination = Table(
    "medical_examinations",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(100)),
    Column("lastname", String(100)),
    Column("specialties", String(255)),
)
