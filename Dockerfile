FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY logs ./logs
COPY functions.py .
COPY main.py .
COPY config.py .


CMD ["python", "-u", "main.py"]


