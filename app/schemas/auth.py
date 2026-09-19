from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


"""

O login deve:

1. Receber email e senha
2. Procurar usuarios
3. Verificar senha com bcrpyt
4. Criar JWT
5. Retomar token.

"""
