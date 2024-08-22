from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from api.core.config import settings
from api.core.database import Base

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


"""
Import all models here to ensure they are included in the migration
"""
from api.user import models  # noqa

target_metadata = Base.metadata


def get_url() -> str:
    return str(settings.DB_URI)


def run_migrations_offline() -> None:
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
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
