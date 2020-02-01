# Latest python
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./src .

# TODO: use conditional building for dev
RUN pip install -r requirements.txt -r requirements.dev.txt

CMD ["flask", "run", "--host=0.0.0.0"]