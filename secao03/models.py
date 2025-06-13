from typing import Optional
from pydantic import BaseModel, Field



class User(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

