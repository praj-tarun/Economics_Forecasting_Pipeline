FROM python:3
COPY . /app
WORKDIR /app
CMD python3 main.py