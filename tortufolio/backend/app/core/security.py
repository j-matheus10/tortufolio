from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.core.config import settings

# --- Configuración de hasheo ---
# schemes=["bcrypt"]: algoritmo que usamos (RNF-05)
# deprecated="auto": si en el futuro cambiamos a argon2, bcrypt se marca como obsoleto
#                     y las contraseñas se re-hashean automáticamente en el próximo login
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- Configuración de JWT ---
ALGORITHM = "HS256"              # Algoritmo de firma: HMAC con SHA-256
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Duración del token: 60 minutos

def hash_password(plain_password: str) -> str:
    """
    Recibe la contraseña en texto plano y devuelve el hash bcrypt.
    Nunca se guarda el texto plano — solo este hash va a la BD.
    """
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Compara la contraseña que el usuario escribió en el login
    contra el hash guardado en la BD.
    Devuelve True si coinciden, False si no.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """
    Genera un token JWT firmado.
    data ejemplo: {"sub": "usuario@email.com", "rol": "gestor"}
    """
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict:
    """
    Lee y verifica un token JWT.
    Si es inválido o expiró, lanza JWTError.
    """
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
