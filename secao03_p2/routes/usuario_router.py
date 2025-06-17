from fastapi import APIRouter


router = APIRouter()

@router.get('/api/v1/usuarios',
            description="Lista de usuários disponíveis",
            summary="Listagem de usuários",
            response_description='Usuários encontrados com sucesso')
async def get_usuarios():
    return {"message": "Lista de usuários"}