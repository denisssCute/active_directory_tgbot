import mysql.connector
import json
# import os


# db_host = os.environ.get('DB_HOST')
# db_port = os.environ.get('DB_PORT')
# db_user = os.environ.get('DB_USER')
# db_password = os.environ.get('DB_PASSWORD')
# db_name = os.environ.get('DB_NAME')



def put(info):
    connect = mysql.connector.connect(user='apiuser', password='apiuser', host='mysql', port='3306', database='bazis')
    db = connect.cursor()
    query = "INSERT INTO users (info, created) VALUES (%s, 0);"
    db.execute(query, (json.dumps(info)))
    connect.commit()
    connect.close()
    return True

def get():
    connect = mysql.connector.connect(user='apiuser', password='apiuser', host='mysql', port='3306', database='bazis')
    db = connect.cursor()
    db.execute("SELECT id, info  FROM users WHERE users.created = 0 ORDER BY id DESC LIMIT 1;")
    data = db.fetchall()

    id_person = data[0][0]

    query = f"UPDATE users SET created = 1 WHERE id = {id_person}"
    db.execute(query)
    connect.commit()

    connect.close()
    return data[0][1]