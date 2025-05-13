from logging.config import fileConfig
from alembic import context
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
import os
import sys
from src.auth.models import Base
from src.transactions.models import Base


# Добавляем путь к проекту
sys.path.append(os.getcwd())


config = context.config
fileConfig(config.config_file_name) if config.config_file_name else None
target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    connectable = create_async_engine(os.getenv("DATABASE_URL"))
    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    do_run_migrations(None)
else:
    asyncio.run(run_async_migrations())