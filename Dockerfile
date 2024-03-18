# Author: Mohamed Elafifi (22066939)
FROM python:3.10 AS prod
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src ./src


FROM prod AS test
COPY ./tests ./tests