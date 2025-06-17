from typing import Dict, List, Optional, Any

from fastapi.responses import JSONResponse
from fastapi import  Path, Query, Header, Depends
from fastapi import FastAPI, HTTPException
from fastapi import status

from time import sleep

from models import Curso
from models import cursos
import asyncio


async def fake_db():
    try:
        print("Conectando ao banco de dados...")
        await asyncio.sleep(0.5)
    finally:
        print("Desconectando do banco de dados...")
        await asyncio.sleep(0.5)

app = FastAPI(
    title="API de Cursos",
    version="0.0.1",
    description="API para estudo de FastAPI",
    contact={
        "name": "Gabriel Romeiro",
        "email": "gabriel.romeiro@example.com"
    }
)


# Métodos GET!
@app.get("/", 
         description="Bem vindo à API de testes do FastAPI", 
         summary="Mensagem de boas-vindas"
)
async def get_msg():
    return {"AVISO": "Api's estão em desenvolvimento, não utilize em produção!"}


@app.get("/cursos", 
         description="Lista de cursos disponíveis, ou uma lista vazia se não houver cursos", 
         summary="Listagem de cursos",
         response_model= List[Curso],
         response_description='Cursos encontrados com sucesso'
)

async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

# Método com HttpException e status

@app.get("/cursos/{curso_id}",
         description="Precisa do ID do curso para buscar", 
         summary="Busca curso por ID",
         response_model= Curso,
)
async def get_curso(
    curso_id: int = Path(
        ...,         
        title="ID do curso", 
        description="Deve ser entre 1 e 4", 
        gt=0, 
        lt=5
    ),
    db: Any = Depends(fake_db)
):
    try:
        curso = cursos[curso_id - 1] 
        curso.id = curso_id
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não encontrado")
    return curso

# Método POST!
@app.post("/cursos", 
          status_code=status.HTTP_201_CREATED, 
          response_model= Curso,
          description="Cria um novo curso",
          summary="Criação de curso"
)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    curso.id = len(cursos) + 1  
    cursos.append(curso)        
    return curso


# Método PUT!
@app.put('/cursos/{curso_id}',
         description="Atualiza um curso existente",
         summary="Atualização de curso",
         response_model= Curso,
)
async def put_curso(
    curso_id: int,
    curso: Curso,
    db: Any = Depends(fake_db)
):
    index = curso_id - 1  

    if 0 <= index < len(cursos):
        curso.id = curso_id  
        cursos[index] = curso
        return curso
    else:
        raise HTTPException(
            status_code=404,
            detail="Curso não existente"
        )

# Método DELETE!
@app.delete('/cursos/{curso_id}',
         description="Remove um curso existente",
         summary="Remoção de curso",
         response_model= List[Curso],
)
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                            content={"msg": "Curso removido com sucesso"})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            
                            detail=f"Não existe curso {curso_id} para ser removido")
    
# Método GET com Query Parameters
@app.get("/calculadora",
         description="Calcula a soma de dois números inteiros",
         summary="Soma de dois números"
)
async def calcular(
    a: int = Query(..., gt=0), 
    b: int = Query(..., gt=0),
    x_geek: Optional[str] = Header(None), 
    c: Optional[int] = Query(None, gt=5)
):
    soma: int = a + b
    if c:
        soma = soma + c
    print(f"X-Geek: {x_geek}")
    return {"resultado": soma}




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)