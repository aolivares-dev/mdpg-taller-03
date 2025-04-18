# app/database.py

from decouple import config
from sqlalchemy import create_engine, MetaData
from databases import Database

# 1. Leer variables de entorno
DATABASE_HOST     = config("DATABASE_HOST")
DATABASE_PORT     = config("DATABASE_PORT", cast=int)
DATABASE_USER     = config("DATABASE_USER")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_NAME     = config("DATABASE_NAME")

# 2. Construir la URL de conexión (usando mysqlconnector)
DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# 3. Instancia asíncrona para FastAPI
database = Database(DATABASE_URL)

# 4. Metadata de SQLAlchemy para definir tablas
metadata = MetaData()

# 5. Instancia sincrónica de Engine
engine = create_engine(DATABASE_URL)  # ← Aquí va
