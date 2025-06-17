from fastapi import APIRouter


router = APIRouter()

@router.get('/api/v1/cursos',
            description="Lista de cursos disponíveis",
            summary="Listagem de cursos",
            response_description='Cursos encontrados com sucesso')
async def get_cursos():
    return {"message": "Lista de cursos"}