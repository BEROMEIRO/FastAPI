from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router

app: FastAPI = FastAPI(
    title='FastAPI SQL Model',
    version="0.0.1",
    description="API desenvolvida para estudo do FastAPI com SQLModel",
    contact={
        "name": "Gabriel Romeiro",
        "email": "gabriel.romeiro@example.com"
    }
)
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,
                host="127.0.0.1", 
                port=8000, 
                log_level='info', 
                reload=True
            )