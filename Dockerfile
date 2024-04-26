FROM python:3.11.6

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y tzdata sqlite3


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

