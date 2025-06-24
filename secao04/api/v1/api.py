from fastapi import APIRouter, HTTPException, status, Depends
from api.v1.endpoints import curso

api_router = APIRouter()
api_router.include_router(curso.router, prefix="/cursos", tags=["cursos"])

# api/v1/cursos