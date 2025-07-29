from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha: str, senha_hash: str) -> bool:
    """
    Verifica se a senha fornecida corresponde ao hash da senha armazenada.

    :param senha: A senha fornecida pelo usuário.
    :param senha_hash: O hash da senha armazenada.
    :return: True se a senha corresponder, False caso contrário.
    """
    return CRIPTO.verify(senha, senha_hash),

def gerar_hash_senha(senha: str) -> str:
    """
    Gera um hash para a senha fornecida.

    :param senha: A senha a ser hasheada.
    :return: O hash da senha.
    """
    return CRIPTO.hash(senha)