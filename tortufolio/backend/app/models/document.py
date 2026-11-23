from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, AuditMixin


class Document(AuditMixin, Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)       # Ruta en el volumen Docker
    file_type = Column(String(50), nullable=False, index=True)  # pdf, docx, xlsx...
    file_size = Column(BigInteger, nullable=False)         # Tamaño en bytes
    version = Column(Integer, default=1)

    # FK: cada documento pertenece a un proyecto
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)

    # Relación
    project = relationship("Project", back_populates="documents")
