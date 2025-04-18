from decouple import config
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_HOST     = config("DATABASE_HOST")
DATABASE_PORT     = config("DATABASE_PORT", cast=int)
DATABASE_USER     = config("DATABASE_USER")
DATABASE_PASSWORD = config("DATABASE_PASSWORD")
DATABASE_NAME     = config("DATABASE_NAME")

DATABASE_URL = (
    f"mysql+mysqlconnector://"
    f"{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

database = Database(DATABASE_URL)

metadata = MetaData()

engine = create_engine(DATABASE_URL)
