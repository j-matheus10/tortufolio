from sqlalchemy import Column, Integer, String, Boolean, Enum as SAEnum
from sqlalchemy.orm import relationship

from app.models.base import Base, AuditMixin
from app.core.enums import RolUsuario, Facultad


class User(AuditMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=False)
    facultad = Column(
        SAEnum(Facultad),       # SAEnum convierte nuestro enum de Python a un tipo
        nullable=False,         # ENUM de PostgreSQL — la BD misma rechaza valores inválidos
    )
    rol = Column(SAEnum(RolUsuario), nullable=False, default=RolUsuario.visualizador)
    is_active = Column(Boolean, default=True)

    # Relación: un usuario puede tener muchos proyectos
    projects = relationship("Project", back_populates="owner")
