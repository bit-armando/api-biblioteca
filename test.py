from sqlalchemy import create_engine

connection_string = "mssql+pyodbc://sa:yourStrong#Password@localhost/biblioteca?driver=ODBC+Driver+17+for+SQL+Server"

# Crear el motor de conexión
engine = create_engine(connection_string)