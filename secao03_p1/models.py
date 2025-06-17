from typing import Optional
from pydantic import BaseModel
from pydantic import field_validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    def validar_titulo(cls, value): #cls é classe
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError("O título deve conter pelo menos 3 palavras.")
        return value

cursos = [
    Curso(id=1, titulo="Programação para Iniciantes", aulas=10, horas=20),
    Curso(id=2, titulo="Python para Iniciantes", aulas=15, horas=30),
    Curso(id=3, titulo="Java para Iniciantes", aulas=12, horas=25),
    Curso(id=4, titulo="JavaScript para Iniciantes", aulas=8, horas=18),
]
