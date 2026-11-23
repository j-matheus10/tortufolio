"""add_facultad_to_users

Revision ID: de2ed0d53818
Revises: 2c9a0fba04d2
Create Date: 2026-11-23 17:36:36.092416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de2ed0d53818'
down_revision: Union[str, None] = '2c9a0fba04d2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Definimos el tipo ENUM como objeto para poder crearlo y eliminarlo
facultad_enum = sa.Enum(
    'ciencias_sociales', 'economia_y_negocios', 'educacion',
    'filosofia_y_humanidades', 'ingenieria', 'derecho',
    name='facultad',
)


def upgrade() -> None:
    # Paso 1: crear el tipo ENUM en PostgreSQL
    facultad_enum.create(op.get_bind(), checkfirst=True)
    # Paso 2: agregar la columna que usa ese tipo
    op.add_column('users', sa.Column('facultad', facultad_enum, nullable=False))


def downgrade() -> None:
    # Paso 1: eliminar la columna
    op.drop_column('users', 'facultad')
    # Paso 2: eliminar el tipo ENUM de PostgreSQL
    facultad_enum.drop(op.get_bind(), checkfirst=True)
