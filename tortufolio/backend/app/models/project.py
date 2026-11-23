from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.models.base import Base, AuditMixin


class Project(AuditMixin, Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(String(50), default="en_progreso")

    # FK: cada proyecto pertenece a un usuario (owner)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relaciones
    owner = relationship("User", back_populates="projects")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
