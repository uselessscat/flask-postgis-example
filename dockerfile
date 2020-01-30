# Latest :)
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY ./src .
RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]