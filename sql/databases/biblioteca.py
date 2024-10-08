from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import contains_eager, sessionmaker

connection_string = "mssql+pyodbc://sa:yourStrong#Password@localhost/biblioteca?driver=ODBC+Driver+17+for+SQL+Server"

# Crear el motor de conexión
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

