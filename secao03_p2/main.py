from fastapi import FastAPI

from routes import curso_router
from routes import usuario_router
from routes import home
from routes import test



app = FastAPI(
    title="API de Cursos",
    version="0.0.1",
    description="API para estudo de FastAPI",
    contact={
        "name": "Sarah Aciole",
        "email": "sarah.aciole@example.com"
    }
)
app.include_router(home.router, tags=["Home"])
app.include_router(test.router, tags=["Home"])
app.include_router(curso_router.router, tags=["Cursos"])
app.include_router(usuario_router.router, tags=["Usuários"])



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)