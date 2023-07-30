FROM python:3.8

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install Flask waitress mysql-connector-python

EXPOSE 999

CMD ["waitress-serve", "--host=0.0.0.0", "--port=999", "main:app"]