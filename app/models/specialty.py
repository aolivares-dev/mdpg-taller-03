# app/models/especialidad.py

from sqlalchemy import Table, Column, Integer, String, Text
from app.database import metadata

# Definir la tabla de especialidades
specialty = Table(
   "specialties",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(100), nullable=False),
    Column("description", Text, nullable=True)
)
