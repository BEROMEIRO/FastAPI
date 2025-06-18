from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/test_api", 
    description="Verifica se a API está funcionando corretamente", 
    summary="API Teste de Funcionamento"
)
async def get_msg():
    return {"AVISO": "Api está funcionando corretamente!"}
