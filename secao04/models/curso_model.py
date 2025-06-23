from core.configs import settings
from sqlalchemy import Column, Integer, String

class CursoModel(settings.DBBaseModel):
    __tablename__ = "cursos" # Nome da tabela no banco de dados

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100), nullable=False)
    aulas: int = Column(Integer, nullable=False)
    horas: int = Column(Integer, nullable=False)