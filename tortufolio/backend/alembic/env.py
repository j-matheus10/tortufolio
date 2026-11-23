from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os

# Importa tus modelos para que Alembic los "vea"
from app.models import Base

config = context.config

# Toma la URL de BD desde la variable de entorno
# Nota: Alembic corre de forma síncrona, así que usamos psycopg2, no asyncpg
database_url = os.getenv("DATABASE_URL", "")
if database_url.startswith("postgresql+asyncpg"):
    database_url = database_url.replace("postgresql+asyncpg", "postgresql+psycopg2", 1)

config.set_main_option("sqlalchemy.url", database_url)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata  # <-- Alembic compara esto vs. la BD real


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
