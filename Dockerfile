FROM python:3.11-slim

WORKDIR /app

COPY current_time.py .

RUN pip install --no-cache-dir flask pytz

# Создать папку для логов и дать права на запись
RUN mkdir -p /var/log/current-time && chmod 777 /var/log/current-time

EXPOSE 1001

CMD ["python", "current_time.py"]
