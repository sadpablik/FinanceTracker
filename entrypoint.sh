#!/bin/bash
set -e

# Ожидание PostgreSQL
echo "Waiting for PostgreSQL..."
while ! pg_isready -h db -U ${DB_USER} -d ${DB_NAME} -t 1; do
  sleep 1
done
echo "PostgreSQL ready!"

# Добавляем текущую директорию в PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Миграции
if [ "$RUN_MIGRATIONS" = "true" ]; then
  echo "Running migrations..."
  alembic upgrade head
fi

# Запуск приложения
echo "Starting application..."
exec uvicorn main:app --host 0.0.0.0 --port 8000