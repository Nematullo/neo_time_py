FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 1001

CMD ["python", "app.py"]
