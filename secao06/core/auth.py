from pytz import timezone
from typing import Optional, List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.future import select


from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt  

from models.usuario.model import UsuarioModel
from core.configs import settings
from core.security import verificar_senha

from pydantic import BaseModel, EmailStr

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticar(email:EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    """
    Autentica um usuário com base no email e senha fornecidos.

    :param email: O email do usuário.
    :param senha: A senha do usuário.
    :param db: A sessão do banco de dados.
    :return: O modelo do usuário autenticado ou None se a autenticação falhar.
    """
    async with db() as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalar_one_or_none()

        if not usuario:
            return None
        
        if not verificar_senha(senha, usuario.senha):
            return None
        return usuario
    
def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    # https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3
    """
    Cria um token JWT.

    :param tipo_token: O tipo do token (ex: 'access', 'refresh').
    :param tempo_vida: O tempo de vida do token.
    :param sub: O assunto do token (geralmente o email do usuário).
    :return: O token JWT gerado.
    """
    payload = {}
    sp = timezone(settings.TIMEZONE)
    expira = datetime.now(tz=sp) + tempo_vida
    
    payload["type"] = tipo_token
    payload["exp"] = expira
    payload["iat"] = datetime.now(tz=sp)
    payload["sub"] = str(sub)

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:
    return _criar_token("access", settings.ACCESS_TOKEN_EXPIRE, sub)

def criar_token_refresh(sub: str) -> str:
    return _criar_token("refresh", settings.REFRESH_TOKEN_EXPIRE, sub)
