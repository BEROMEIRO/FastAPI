from typing import Optional
from pydantic import BaseModel, field_validator
class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int  # mais de 12 aulas
    horas: int  # mais de 10 horas

    @field_validator('titulo')
    def validar_titulo(cls, value: str):
        #validação 1 verificando se o títulos possui pelo menos 3 palavras
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError("O título deve conter pelo menos 3 palavras.")
        
        #validação 2 verificando se o título possui pelo menos uma letra maiúscula
        if value.islower():
            raise ValueError("O título deve conter pelo menos uma letra maiúscula.")
       
        return value
    
    #validação 3 verificando se aulas são maiores que 12
    @field_validator('aulas')
    @classmethod
    def validar_aulas(cls, value: int):
        if value <= 12:
            raise ValueError("O número de aulas deve ser maior que 12.")
        return value

    #validação 4 verificando se horas são maiores que 10
    @field_validator('horas')
    @classmethod
    def validar_horas(cls, value: int):
        if value <= 10:
            raise ValueError("O número de horas deve ser maior que 10.")
        return value
    
# Dados fake
cursos = [
    Curso(id=1, titulo="Programação para Iniciantes", aulas=14, horas=20),
    Curso(id=2, titulo="Python para Iniciantes", aulas=15, horas=30),
    Curso(id=3, titulo="Java para Iniciantes", aulas=13, horas=25),
    Curso(id=4, titulo="JavaScript para Iniciantes", aulas=13, horas=18),
    Curso(id=5, titulo="TypeScript para Iniciantes", aulas=13, horas=20),
]
