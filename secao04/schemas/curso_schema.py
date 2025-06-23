from typing import Optional
from pydantic import BaseModel as SCBaseModel


class CursoSchema(SCBaseModel):
    id: Optional[int] # Opcional na criação, obrigatório na resposta
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True # Permite pegar dados do Model (SQLAlchemy) direto

    