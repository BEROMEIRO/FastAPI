from fastapi import FastAPI

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

@app.get("/")
async def get_msg():
    return {"AVISO": "Vá para /cursos para ver a lista de cursos disponíveis"}


@app.get("/cursos")
async def get_cursos():
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: str):

    if not curso_id.isdigit():
        return {"Atenção": "Inserir dados do tipo INT(Número Inteiro)"}

    curso_id = int(curso_id)
    
    curso = cursos.get(curso_id)
    if curso:
        curso.update({"id": curso_id})
        return curso
    return {"error": "Curso não encontrado"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)