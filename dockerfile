FROM python:3.13

WORKDIR /app

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Явно добавляем рабочую директорию в PYTHONPATH
ENV PYTHONPATH=/app

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]