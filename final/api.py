import json

from flask import Flask, request
import sqlite3
from datetime import datetime
import pika
from flask_cors import CORS

RABBIT_URL = "rabbitmq"


app = Flask(__name__)
CORS(app)

connection = sqlite3.connect("data/data.db", check_same_thread=False)

credentials = pika.PlainCredentials('root', '123654789')
rabbit_connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq', port=5672, credentials=credentials))
channel = rabbit_connection.channel()
channel.exchange_declare(exchange='news', exchange_type='direct')


# cursor.execute("CREATE TABLE users (name TEXT, lastname TEXT, phone TEXT, topics TEXT)")
# cursor.execute("CREATE TABLE news (title TEXT, text TEXT, topic TEXT, createdAt timestamp)")


@app.route('/user/create', methods=['POST'])
def createUser():
    global connection

    sql = "INSERT INTO users VALUES ('{}', '{}', '{}', '{}')".format(
        request.json.get("name"), request.json.get("lastname"), request.json.get("phone"), request.json.get("topics"))

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

    return "ok"


@app.route('/user/topics', methods=['GET'])
def getUserTopics():
    global connection

    sql = "SELECT topics FROM users WHERE phone='{}'".format(request.args.get("phone"))

    cursor = connection.cursor()
    row = cursor.execute(sql).fetchall()[0]

    return row[0].split(",")


@app.route('/admin/news/create', methods=['POST'])
def createNews():
    global connection, channel

    sql = "INSERT INTO news VALUES ('{}', '{}', '{}', '{}')".format(
        request.json.get("title"), request.json.get("text"), request.json.get("topic"), datetime.now())

    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

    message = {
        "title": request.json.get("title"),
        "text": request.json.get("text"),
        "topic": request.json.get("topic"),
        "createdAt": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    channel.basic_publish(exchange='news', routing_key=request.json.get("topic"), body=json.dumps(message))
    print(f" [x] Sent {request.json.get('topic')}:{request.json.get('title')}")
    return "ok"


