from pydantic import BaseModel
from typing import Optional

class Editorial(BaseModel):
    nombre: str


class Autor(BaseModel):
    nombre: str
    apellido_p: str
    apellido_m: str

#
# class Direcciones(BaseModel):
#     calle: str
#     num_ext: int
#     num_int: int
#     colonia: str
#     cp: int
#
#
# class Libros_CAT(BaseModel):
#     categoria: str
#
#
# class Usuario_CAT(BaseModel):
#     categoria: str
#
#
# class Usuario(BaseModel):
#     nombre: str
#     apellido_p: str
#     apellido_m: Optional[str]
#     telefono: str
#     email: str
#     multa: float(2)
#     direccion: int
#     tipo: int
#     is_activate: bool
#
#
# class Libros(BaseModel):
#     ISBN: str
#     titulo: str
#     autor: int
#     categoria: int
#     editorial: int
#     # fecha_pub = Column(Date)
#     copias: int