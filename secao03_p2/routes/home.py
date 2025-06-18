from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/", 
    description="Bem vindo à API de testes do FastAPI", 
    summary="Mensagem de boas-vindas"
)
async def get_msg():
    return {"AVISO": "Api's estão em desenvolvimento, não utilize em produção!"}
