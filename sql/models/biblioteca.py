from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from sql.databases.biblioteca import Base
from sql.databases.biblioteca import engine



class Editorial(Base):
    __tablename__ = 'editorial'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)


class Autor(Base):
    __tablename__ = 'AUTOR'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido_p = Column(String)
    apellido_m = Column(String)


# class Direcciones(Base):
#     __tablename__ = 'direcciones'
#
#     id = Column(Integer, primary_key=True)
#     calle  = Column(String, nullable=False)
#     num_ext = Column(Integer)
#     num_int = Column(Integer)
#     colonia = Column(String, nullable=False)
#     cp = Column(Integer)
#
# class Libros_Categoria(Base):
#     __tablename__ = 'libros_cat'
#
#     id = Column(Integer, primary_key=True)
#     categoria = Column(String, nullable=False)
#
#
# class Usuario_Categoria(Base):
#     __tablename__ = 'usuario_cat'
#
#     id = Column(Integer, primary_key=True)
#     categoria = Column(String, nullable=False)
#
#
# class Usuario(Base):
#     __tablename__ = 'usuario'
#
#     id = Column(Integer, primary_key=True)
#     nombre = Column(String, nullable=False)
#     apellido_p = Column(String, nullable=False)
#     apellido_m = Column(String)
#     telefono = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     multa = Column(DECIMAL(precision=2), nullable=False)
#     direccion = Column(Integer, ForeignKey('direcciones.id'), nullable=False)
#     tipo = Column(Integer, ForeignKey('usuario_cat.id'), nullable=False)
#     is_activate = Column(Boolean)
#
#
# class Libros(Base):
#     __tablename__ = 'libros'
#     ISBN = Column(String, nullable=False, primary_key=True)
#     titulo = Column(String, nullable=False)
#     autor = Column(Integer, ForeignKey('autor.id'), nullable=False)
#     categoria = Column(Integer, ForeignKey('libros_cat.id'), nullable=False)
#     editorial = Column(Integer, ForeignKey('editorial.id'), nullable=False)
#     # fecha_pub = Column(Date)
#     copias = Column(Integer)

Base.metadata.create_all(bind=engine)