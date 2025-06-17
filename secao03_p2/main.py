from fastapi import FastAPI

from routes import curso_router
from routes import usuario_router

app = FastAPI(
    title="API de Cursos",
    version="0.0.1",
    description="API para estudo de FastAPI",
    contact={
        "name": "Gabriel Romeiro",
        "email": "gabriel.romeiro@example.com"
    }
)
app.include_router(curso_router.router, tags=["Cursos"])
app.include_router(usuario_router.router, tags=["Usuários"])


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)