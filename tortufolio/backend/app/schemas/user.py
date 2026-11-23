from pydantic import BaseModel, EmailStr, Field
from app.core.enums import RolUsuario, Facultad


class UserCreate(BaseModel):
    """Schema para registrar un usuario nuevo (POST /register)."""
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    full_name: str = Field(min_length=2, max_length=150)
    facultad: Facultad
    rol: RolUsuario = RolUsuario.visualizador


class UserRead(BaseModel):
    """Schema para devolver datos de un usuario (respuesta de la API)."""
    id: int
    email: EmailStr
    full_name: str
    facultad: Facultad
    rol: RolUsuario
    is_active: bool

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    """Schema para actualizar un usuario (PUT/PATCH)."""
    full_name: str | None = None
    facultad: Facultad | None = None
    rol: RolUsuario | None = None
    is_active: bool | None = None


class Token(BaseModel):
    """Schema para la respuesta del login."""
    access_token: str
