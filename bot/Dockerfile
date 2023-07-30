FROM python:3.8

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN pip install --upgrade pip
RUN pip install telebot mysql-connector-python paramiko

EXPOSE 8080

CMD ["python", "bot.py"]
