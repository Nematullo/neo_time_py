FROM python:3.11-slim

WORKDIR /app

COPY current_time.py .

RUN pip install --no-cache-dir flask pytz

EXPOSE 1001

CMD ["python", "current_time.py"]
