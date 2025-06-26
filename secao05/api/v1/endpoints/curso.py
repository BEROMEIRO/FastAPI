from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.curso_model import CursoModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True # type: ignore

#End of bypass warning

router = APIRouter()

# POST CURSO
@router.post(
    "/",
    response_model=CursoModel,
    status_code=status.HTTP_201_CREATED,
    tags=["cursos"]
)
async def post_curso(curso: CursoModel, db: AsyncSession = Depends(get_session)):
    novo_curso = CursoModel(titulo=curso.titulo,aulas=curso.aulas, horas=curso.horas)
    db.add(novo_curso)
    await db.commit()
    await db.refresh(novo_curso)
    return novo_curso

#GET CURSOS
@router.get(
    "/",
    response_model=List[CursoModel],
    status_code=status.HTTP_200_OK,
    tags=["cursos"]
)
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List[CursoModel] = result.scalars().all()
        return cursos
    
#GET CURSO BY ID
@router.get(
    "/{curso_id}",
    response_model=CursoModel,
    status_code=status.HTTP_200_OK,
    tags=["cursos"]
)
async def get_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso: CursoModel = result.scalar_one_or_none()
        if curso:
            return curso
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não encontrado")
    
#PUT CURSO
@router.put("/{curso_id}", 
            status_code=status.HTTP_202_ACCEPTED,
            response_model=CursoModel,
            tags=["cursos"]
)
async def put_curso(
    curso_id: int, 
    curso: CursoModel, 
    db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_up: CursoModel = result.scalar_one_or_none()
        if curso_up:
            curso_up.titulo = curso.titulo
            curso_up.aulas = curso.aulas
            curso_up.horas = curso.horas
            await session.commit()
            await session.refresh(curso_up)
            return curso_up
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não encontrado")
    

#DELETE CURSO
@router.delete("/{curso_id}",
               status_code=status.HTTP_204_NO_CONTENT,
               tags=["cursos"]
)
async def delete_curso(curso_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == curso_id)
        result = await session.execute(query)
        curso_del: CursoModel = result.scalar_one_or_none()
        if curso_del:
            await session.delete(curso_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Curso não encontrado")