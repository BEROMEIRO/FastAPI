from typing import List, Optional

from fastapi.responses import JSONResponse
from fastapi import  Path, Query, Header
from fastapi import FastAPI, HTTPException, status

from models import Curso


app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Iniciantes",	
        "aulas": 10,
        "horas": 20
    },
    2: {
        "titulo": "Python para Iniciantes",	
        "aulas": 15,
        "horas": 30
    },
}

# Métodos GET!
@app.get("/")
async def get_msg():
    return {"AVISO": "Vá para /cursos para ver a lista de cursos disponíveis"}


@app.get("/cursos")
async def get_cursos():
    return cursos

# Método com HttpException e status

@app.get("/cursos/{curso_id}")
async def get_curso(
    curso_id: int = Path(
        ..., 
        title="ID do curso", 
        description="Deve ser entre 1 e 2", 
        gt=0, 
        lt=3
    )
):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não encontrado")
    return curso

# Método POST!
@app.post("/cursos", status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

# Método PUT!
@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não existente")

# Método DELETE!
@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return JSONResponse(status_code=status.HTTP_202_ACCEPTED,
                            content={"msg": "Curso removido com sucesso"})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            
                            detail=f"Não existe curso {curso_id} para ser removido")
# Método GET com Query Parameters
@app.get("/calculadora")
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