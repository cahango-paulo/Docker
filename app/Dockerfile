FROM python:3.11-alpine


RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev


RUN adduser -D -g "" appuser


WORKDIR /app


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY . ./

USER appuser

CMD ["python", "main.py"]

