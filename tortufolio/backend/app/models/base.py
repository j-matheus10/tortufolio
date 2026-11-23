from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Clase base de la que heredan todos los modelos."""
    pass


class AuditMixin:
    """
    Mixin de auditoría (RS-04).
    Cualquier modelo que herede de esto tendrá automáticamente:
    - created_at: fecha de creación (se llena solo)
    - updated_at: fecha de última modificación (se actualiza solo)
    - updated_by: quién hizo el último cambio
    """
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),  # PostgreSQL pone la fecha al insertar
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),  # Se actualiza automáticamente al modificar
        nullable=False,
    )
    updated_by = Column(String, nullable=True)  # user_id de quién modificó
