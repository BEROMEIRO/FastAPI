from typing import Optional
from pydantic import BaseModel, Field

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

